# AI Physician Notetaker - README

## Overview
The AI Physician Notetaker is a Python-based tool that processes medical transcripts to extract relevant insights such as symptoms, treatments, diagnoses, prognosis, sentiment, and intent. It also generates a structured SOAP (Subjective, Objective, Assessment, Plan) note and saves the output in a JSON file.

This project leverages NLP models from **SpaCy, Transformers, and Sentence-Transformers** to automate medical documentation.

Repository Link: [GitHub - Physician Notemaker](https://github.com/DattatrayBodake25/physician-notemaker)

---

## Features
- **Transcript Cleaning**: Removes unnecessary newlines and unwanted text blocks.
- **Named Entity Recognition (NER)**: Extracts medical terms related to symptoms, treatment, diagnosis, and prognosis.
- **Summarization**: Generates a concise summary of the transcript.
- **Keyword Extraction**: Identifies the most relevant medical keywords.
- **Sentiment Analysis**: Detects whether the patient is anxious, reassured, or neutral.
- **Intent Detection**: Classifies the patient’s intent (e.g., reporting symptoms, seeking reassurance, etc.).
- **SOAP Note Generation**: Converts extracted insights into a structured SOAP format.
- **Final JSON Output**: Stores all extracted data in `final_output.json`.

---

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed.

### 1. Clone the Repository
```sh
git clone https://github.com/DattatrayBodake25/physician-notemaker.git
cd physician-notemaker
```

### 2. Install Dependencies
Run the following command to install all required libraries:
```sh
pip install -r requirements.txt
```
Or manually install:
```sh
pip install transformers spacy scikit-learn sentence-transformers torch nltk
```

### 3. Download SpaCy Model
```sh
python -m spacy download en_core_web_sm
```

### 4. Run the Notebook
Ensure you have a medical transcript file (`sample_transcript.txt`) in the project directory. Then execute the **Physician Notemaker.ipynb** notebook step by step in Jupyter Notebook.

---

## Usage in Jupyter Notebook
If you prefer to run the script in Jupyter Notebook, follow these steps:
```sh
pip install jupyter
jupyter notebook
```
Then, open `Physician Notemaker.ipynb`, follow the steps, and execute the cells sequentially.

---

## Output
After execution, the program generates a structured **SOAP note** and stores all extracted information in a JSON file:
```
final_output.json
```
Example output:
```json
{
    "Summary": "The patient reports mild neck pain after a car accident...",
    "NER_Results": {
        "Symptoms": ["neck pain"],
        "Treatment": ["painkillers"],
        "Diagnosis": ["whiplash"],
        "Prognosis": ["recovery"]
    },
    "Sentiment": "Anxious",
    "Intent": "Reporting symptoms",
    "SOAP_Note": { ... }
}
```

---

## Troubleshooting
- **Issue with SpaCy import?** Run:
  ```sh
  pip uninstall spacy -y && pip install spacy
  ```
- **ModuleNotFoundError?** Ensure dependencies are installed:
  ```sh
  pip install -r requirements.txt
  ```
- **Jupyter Kernel Crashes?** Restart and rerun cells sequentially.

---

---

## Contributing
1. Fork the repository.
2. Create a new feature branch.
3. Commit changes and submit a PR.

---
