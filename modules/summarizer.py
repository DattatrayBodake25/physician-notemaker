from transformers import pipeline, Pipeline

# Load summarization model
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    raise RuntimeError(f"Failed to load summarization model: {e}")

def summarize_transcript(text):
    """
    Summarizes a given medical transcript using a pre-trained DistilBART model.

    Args:
        text (str): Input medical transcript text

    Returns:
        str: Clean and summarized version of the transcript
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input text must be a non-empty string.")

    try:
        # Generate summary
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)

        if not summary or 'summary_text' not in summary[0]:
            raise RuntimeError("Summarization failed: No summary text generated.")

        clean_summary = summary[0]['summary_text'].replace('"', '').strip()

        # Remove duplicate sentences while preserving order
        sentences = list(dict.fromkeys(clean_summary.split('. ')))  # Use dict for order preservation
        clean_summary = '. '.join(sentences)

        return clean_summary

    except Exception as e:
        raise RuntimeError(f"Error during summarization: {e}")

# Example usage (for debugging purposes)
if __name__ == "__main__":
    sample_text = """
    The patient had a car accident and experienced neck pain and stiffness. 
    The patient was treated with physiotherapy and painkillers. 
    After several sessions, the patient's condition improved significantly.
    """
    try:
        result = summarize_transcript(sample_text)
        print("Summary:\n", result)
    except Exception as e:
        print(f"Error: {e}")