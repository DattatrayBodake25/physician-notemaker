import spacy
from spacy.matcher import PhraseMatcher

# Load the spaCy model
try:
    nlp = spacy.load('en_core_web_sm')
except Exception as e:
    raise RuntimeError(f"Failed to load spaCy model: {e}")

def extract_medical_entities(text):
    """
    Extracts medical entities such as Symptoms, Treatment, Diagnosis, and Prognosis
    from a given text using spaCy and PhraseMatcher.

    Args:
        text (str): Input medical transcript text

    Returns:
        dict: A dictionary containing lists of extracted entities:
            - Symptoms
            - Treatment
            - Diagnosis
            - Prognosis
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input text must be a non-empty string.")

    try:
        doc = nlp(text)

        # Initialize PhraseMatcher
        matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

        # Define patterns for medical terms
        symptom_patterns = ["pain", "ache", "stiffness", "discomfort", "headache", 
                            "injury", "whiplash injury", "car accident"]
        treatment_patterns = ["physiotherapy", "session", "medication", "painkillers"]
        diagnosis_patterns = ["fracture", "strain", "sprain", "injury", "whiplash injury"]
        prognosis_patterns = ["recovery", "healing", "improve", "resolve"]

        # Add patterns to matcher (handle multi-word terms correctly)
        matcher.add("SYMPTOMS", [nlp.make_doc(pattern) for pattern in symptom_patterns])
        matcher.add("TREATMENT", [nlp.make_doc(pattern) for pattern in treatment_patterns])
        matcher.add("DIAGNOSIS", [nlp.make_doc(pattern) for pattern in diagnosis_patterns])
        matcher.add("PROGNOSIS", [nlp.make_doc(pattern) for pattern in prognosis_patterns])

        # Initialize sets to store matched entities
        symptoms, treatments, diagnoses, prognoses = set(), set(), set(), set()

        # Find matches in the document
        matches = matcher(doc)
        for match_id, start, end in matches:
            match_text = doc[start:end].text
            label = nlp.vocab.strings[match_id]
            if label == "SYMPTOMS":
                symptoms.add(match_text)
            elif label == "TREATMENT":
                treatments.add(match_text)
            elif label == "DIAGNOSIS":
                diagnoses.add(match_text)
            elif label == "PROGNOSIS":
                prognoses.add(match_text)

        # Infer diagnosis based on symptoms + treatment
        if "pain" in symptoms and "physiotherapy" in treatments:
            diagnoses.add("whiplash injury")

        # Build result dictionary
        result = {
            "Symptoms": sorted(symptoms),
            "Treatment": sorted(treatments),
            "Diagnosis": sorted(diagnoses),
            "Prognosis": sorted(prognoses)
        }

        return result

    except Exception as e:
        raise RuntimeError(f"Error during NER extraction: {e}")

# Example usage (for debugging purposes)
if __name__ == "__main__":
    sample_text = "I had a car accident and experienced neck pain. I took painkillers and underwent physiotherapy."
    try:
        result = extract_medical_entities(sample_text)
        print(result)
    except Exception as e:
        print(f"Error: {e}")