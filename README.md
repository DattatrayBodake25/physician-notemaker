# 🩺 AI Physician Notetaker

## Overview
The **AI Physician Notetaker** is a Python-based NLP application designed to automate the process of medical documentation by extracting structured insights from physician-patient conversations. The system processes medical transcripts to identify key medical terms, classify intent, analyze sentiment, and generate structured SOAP notes in JSON format.

This project leverages advanced **NLP models** from **SpaCy**, **Transformers**, **Sentence-Transformers**, and **Scikit-learn** to extract insights and convert them into a structured format suitable for medical documentation.

---

## 🚀 Features
### ✅ **Transcript Processing**
- Removes unwanted characters, newlines, and noise from the raw transcript for cleaner input.

### ✅ **Named Entity Recognition (NER)**
- Extracts key medical entities from the transcript:
  - **Symptoms** – E.g., pain, stiffness, headache  
  - **Treatment** – E.g., medication, therapy  
  - **Diagnosis** – E.g., whiplash, injury  
  - **Prognosis** – E.g., recovery  

### ✅ **Summarization**
- Uses transformer-based models to generate a concise summary of the conversation.

### ✅ **Keyword Extraction**
- Identifies key medical terms using TF-IDF and other NLP-based techniques.

### ✅ **Sentiment Analysis**
- Classifies the emotional tone of the patient:
  - Positive  
  - Negative  
  - Neutral  

### ✅ **Intent Detection**
- Classifies the patient's intent during the conversation:
  - Reporting symptoms  
  - Seeking reassurance  
  - Requesting medication  

### ✅ **SOAP Note Generation**
- Generates a structured **SOAP (Subjective, Objective, Assessment, Plan)** note using the extracted insights:
  - **Subjective** – Patient’s complaints and history  
  - **Objective** – Observations and physical exam findings  
  - **Assessment** – Diagnosis and severity  
  - **Plan** – Recommended treatment and follow-up  

### ✅ **Structured JSON Output**
- Generates all extracted information in JSON format for easy storage and further processing.

---

## 📂 Project Structure
```
physician-notemaker/
├── modules/                 # Contains all code modules
│   ├── ner.py              # Named entity recognition (NER) module
│   ├── summarizer.py       # Summarization module
│   ├── sentiment.py        # Sentiment analysis module
│   ├── intent.py           # Intent classification module
│   ├── soap.py   # SOAP note generation module
├── app.py                   # Streamlit app for deployment
├── requirements.txt         # Project dependencies
├── sample_transcript.txt    # Sample input transcript
├── README.md                # Project documentation
└── .gitignore               # Git ignore file
```

---

## 🛠️ Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/DattatrayBodake25/physician-notemaker.git
cd physician-notemaker
```

### **2. Create a Virtual Environment (Optional)**
```sh
python -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
Install all necessary libraries:
```sh
pip install -r requirements.txt
```

### **4. Download SpaCy Model**
Include the SpaCy model directly:
```sh
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl
```

---

## 🚀 Running the App
### **1. Start the Streamlit App**
To run the app locally:
```sh
streamlit run app.py
```

### **2. Upload the Transcript**
- Upload a `.txt`, `.pdf`, or `.docx` file.
- Click **"Process Transcript."**

### **3. View Output**
- Extracted insights, SOAP note, and sentiment/intent analysis will be shown in JSON format:
```json
{
  "Summary": "Patient reported neck pain after a car accident...",
  "NER_Results": {
    "Symptoms": ["neck pain", "headache"],
    "Treatment": ["painkillers"],
    "Diagnosis": ["whiplash"],
    "Prognosis": ["recovery"]
  },
  "Sentiment": "Negative",
  "Intent": "Reporting symptoms",
  "SOAP_Note": { ... }
}
```

---

## 🏥 **Approach**
### 1. **Data Cleaning**
- Removed unwanted characters, newlines, and formatting issues.
- Converted text to lowercase for uniform processing.

### 2. **Named Entity Recognition (NER)**
- Used **SpaCy** to detect medical terms related to symptoms, diagnosis, treatment, and prognosis.

### 3. **Summarization**
- Used **Hugging Face Transformers** to summarize conversations.
- Ensured medical terminology was retained.

### 4. **Keyword Extraction**
- Applied **TF-IDF** to identify key terms from the transcript.

### 5. **Sentiment Analysis**
- Used **BERT-based models** to classify sentiment into positive, negative, or neutral.

### 6. **Intent Classification**
- Employed supervised classification to identify the patient's intent (reporting symptoms, reassurance, etc.).

### 7. **SOAP Note Generation**
- Mapped extracted insights into a structured SOAP format.

---

## ✅ Example SOAP Note Output
```json
"SOAP_Note": {
    "Subjective": {
        "Chief_Complaint": "Neck pain and stiffness",
        "History_of_Present_Illness": "Patient experienced neck pain following a car accident..."
    },
    "Objective": {
        "Physical_Exam": "Signs of discomfort in neck and reduced range of motion.",
        "Observations": "Patient is otherwise stable."
    },
    "Assessment": {
        "Diagnosis": "Whiplash",
        "Severity": "Moderate"
    },
    "Plan": {
        "Treatment": "Painkillers and physiotherapy",
        "Follow-Up": "Recommended follow-up in 2 weeks."
    }
}
```

---

## 🚧 Troubleshooting
| Problem | Solution |
|---------|----------|
| **Permission Denied on SpaCy Model Install** | Install model in user directory:<br>`python -m spacy download en_core_web_sm --user` |
| **Module Not Found Error** | Ensure dependencies are installed:<br>`pip install -r requirements.txt` |
| **Streamlit App Not Starting** | Check port availability or restart Streamlit:<br>`streamlit run app.py` |

---

## 🙌 Contributing
1. Fork the repository.
2. Create a new feature branch:
```sh
git checkout -b feature-branch
```
3. Commit changes and push:
```sh
git commit -m "Add new feature"
git push origin feature-branch
```
4. Submit a pull request.

---

## 🏆 Acknowledgements
- Built using **Python**, **SpaCy**, **Transformers**, **Sentence-Transformers**, and **Streamlit**.
- Inspired by real-world challenges in medical documentation automation.

---

## 📃 License
This project is licensed under the **MIT License**.

---

**💙 Built with ❤️ using Python and Streamlit**

