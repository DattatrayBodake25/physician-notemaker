import sys
import asyncio
import warnings
import spacy
from spacy.cli import download

# === Fix torch.classes issue ===
sys.modules['torch._classes'] = None

# === Fix asyncio loop conflict ===
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# === Suppress PyTorch path warnings ===
warnings.filterwarnings("ignore", category=UserWarning, module="torch._classes")

# === Ensure spaCy model is installed ===
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Downloading spaCy model 'en_core_web_sm'...")
    download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')

# === Load spaCy model ===
nlp = spacy.load('en_core_web_sm')

import streamlit as st
import json
import pdfplumber
from io import BytesIO
from docx import Document
from modules.ner import extract_medical_entities
from modules.summarizer import summarize_transcript
from modules.sentiment import analyze_sentiment
from modules.intent import detect_intent
from modules.soap import generate_soap_note

# === Page Config ===
st.set_page_config(page_title="AI Physician Notetaker", page_icon="🩺", layout="wide")

# === HEADER ===
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50;">🩺 AI Physician Notetaker</h1>
    <p style="text-align: center; font-size: 18px; color: #555;">
        Upload a transcript to generate a detailed SOAP note with medical insights
    </p>
    """,
    unsafe_allow_html=True,
)

# === FUNCTION TO READ FILE CONTENT ===
def read_uploaded_file(uploaded_file):
    """
    Reads uploaded file content based on file type.

    Args:
        uploaded_file (UploadedFile): Uploaded file object.

    Returns:
        str: Extracted text from the file.
    """
    try:
        file_type = uploaded_file.name.split('.')[-1].lower()
        content = ""

        uploaded_file.seek(0)  # Reset stream position

        if file_type == 'txt':
            content = uploaded_file.read().decode("utf-8")

        elif file_type == 'pdf':
            with pdfplumber.open(BytesIO(uploaded_file.read())) as pdf:
                content = "\n".join([page.extract_text() or "" for page in pdf.pages])

        elif file_type == 'docx':
            doc = Document(uploaded_file)
            content = "\n".join([para.text for para in doc.paragraphs])

        else:
            st.error(f"🚨 Unsupported file format: {file_type}")
            return None
        
        if not content.strip():
            st.error("❌ File is empty or could not be read. Please check the file content.")
            return None

        return content

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        return None

# === SIDEBAR (for file upload & preview) ===
with st.sidebar:
    st.header("📂 Upload Transcript")
    uploaded_file = st.file_uploader(
        "Upload file", 
        type=["txt", "pdf", "docx"], 
        help="Supported formats: .txt, .pdf, .docx"
    )

    transcript = ""
    if uploaded_file is not None:
        transcript = read_uploaded_file(uploaded_file)
        if transcript:
            st.markdown("### 📝 Transcript Preview")
            st.text_area("Transcript Content", transcript, height=300)

# === PROCESSING LOGIC ===
if transcript:
    if st.button("🚀 Process Transcript", use_container_width=True):
        with st.spinner("⏳ Processing... Please wait"):
            try:
                if len(transcript.split()) < 5:
                    st.error("❌ Transcript is too short to process.")
                    st.stop()

                # --- Step 1: Summarization ---
                summary = summarize_transcript(transcript)
                
                # --- Step 2: NER Extraction ---
                ner_results = extract_medical_entities(transcript)
                
                # --- Step 3: Sentiment Analysis ---
                sentiment = analyze_sentiment(transcript)
                
                # --- Step 4: Intent Detection ---
                intent = detect_intent(transcript)
                
                # --- Step 5: SOAP Note Generation ---
                soap_note = generate_soap_note(summary, ner_results)

                output = {
                    "Summary": summary,
                    "NER_Results": ner_results,
                    "Sentiment": sentiment,
                    "Intent": intent,
                    "SOAP_Note": soap_note
                }

                # --- SUCCESS MESSAGE ---
                st.success("✅ Transcript processed successfully!")

                # --- 📝 DIAGNOSTIC SUMMARY ---
                st.subheader("📝 Diagnostic Summary")
                st.json(output, expanded=True)

                # --- DOWNLOAD BUTTON ---
                st.download_button(
                    label="📥 Download Results",
                    data=json.dumps(output, indent=4),
                    file_name="results.json",
                    mime="application/json",
                    use_container_width=True
                )

            except ValueError as ve:
                st.error(f"❌ Validation Error: {ve}")

            except RuntimeError as re:
                st.error(f"🚨 Processing Error: {re}")

            except Exception as e:
                st.error(f"❌ Unexpected Error: {e}")

# === FOOTER ===
st.markdown(
    """
    <div style="text-align: center; padding-top: 20px; font-size: 14px; color: #999;">
        Built with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
