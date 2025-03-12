def generate_soap_note(summary, ner_results):
    """
    Generates a structured SOAP note based on the summary and extracted medical entities.

    Args:
        summary (str): Summary of the patient's condition.
        ner_results (dict): Extracted medical entities including symptoms, treatment, diagnosis, and prognosis.

    Returns:
        dict: A structured SOAP note containing Subjective, Objective, Assessment, and Plan.
    """
    if not isinstance(summary, str) or not summary.strip():
        raise ValueError("Summary must be a non-empty string.")

    if not isinstance(ner_results, dict):
        raise ValueError("NER results must be provided as a dictionary.")

    symptoms = ner_results.get('Symptoms', [])
    treatment = ner_results.get('Treatment', [])
    diagnosis = ner_results.get('Diagnosis', [])
    prognosis = ner_results.get('Prognosis', [])

    # Set severity based on number of symptoms
    severity = "Mild"
    if len(symptoms) >= 3:
        severity = "Moderate"
    if len(symptoms) > 4:
        severity = "Severe"

    # Adaptive physical exam based on symptoms
    if "pain" in symptoms or "stiffness" in symptoms:
        physical_exam = "Signs of discomfort and limited range of motion."
    else:
        physical_exam = "Full range of motion, no tenderness."

    follow_up = "Full recovery expected within six months."
    if severity == "Severe":
        follow_up = "Regular follow-up recommended due to symptom severity."
    if len(prognosis) == 0:
        follow_up = "Monitoring required due to uncertain prognosis."

    subjective = {
        "Chief_Complaint": ', '.join(symptoms) if symptoms else "No symptoms reported",
        "History_of_Present_Illness": summary.strip()
    }

    objective = {
        "Physical_Exam": physical_exam,
        "Observations": "Patient appears in normal health."
    }

    assessment = {
        "Diagnosis": ', '.join(diagnosis) if diagnosis else "No specific diagnosis identified",
        "Severity": severity
    }

    plan = {
        "Treatment": ', '.join(treatment) if treatment else "No treatment prescribed",
        "Follow-Up": follow_up
    }

    soap_note = {
        "Subjective": subjective,
        "Objective": objective,
        "Assessment": assessment,
        "Plan": plan
    }

    return soap_note

# Example usage (for debugging purposes)
if __name__ == "__main__":
    sample_summary = "Patient was involved in a car accident last month. She experienced neck and back pain."
    sample_ner_results = {
        "Symptoms": ["pain", "stiffness"],
        "Treatment": ["physiotherapy", "painkillers"],
        "Diagnosis": ["whiplash injury"],
        "Prognosis": ["recovery"]
    }
    try:
        soap_note = generate_soap_note(sample_summary, sample_ner_results)
        print("SOAP Note:\n", soap_note)
    except Exception as e:
        print(f"Error: {e}")