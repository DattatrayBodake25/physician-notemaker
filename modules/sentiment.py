from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import numpy as np

# Load model and tokenizer (keep small size)
try:
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")
    sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
except Exception as e:
    raise RuntimeError(f"Failed to load sentiment analysis model: {e}")

def analyze_sentiment(text):
    """
    Analyzes sentiment of the input medical transcript using a DistilBERT model.

    Args:
        text (str): Input text to analyze

    Returns:
        str: Custom sentiment label ("POSITIVE", "REASSURED", "NEUTRAL", "CONCERNED", "NEGATIVE")
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input text must be a non-empty string.")

    try:
        tokens = tokenizer.encode(text, return_tensors="pt")
        max_length = tokenizer.model_max_length

        if tokens.shape[1] > max_length:
            # Split into chunks if input exceeds token limit
            print(f"Input too long ({tokens.shape[1]} tokens). Splitting into chunks...")

            chunks = [text[i:i + max_length] for i in range(0, len(text), max_length)]
            sentiment_scores = []

            for chunk in chunks:
                result = sentiment_pipeline(chunk)[0]
                score = result['score'] if result['label'] == 'POSITIVE' else -result['score']
                sentiment_scores.append(score)

            avg_score = np.mean(sentiment_scores)

        else:
            # Process directly if within token limit
            result = sentiment_pipeline(text)[0]
            avg_score = result['score'] if result['label'] == 'POSITIVE' else -result['score']

        # Custom classification based on score ranges
        if avg_score > 0.5:
            sentiment_label = "POSITIVE"
        elif 0.1 < avg_score <= 0.5:
            sentiment_label = "REASSURED"
        elif -0.1 <= avg_score <= 0.1:
            sentiment_label = "NEUTRAL"
        elif -0.5 <= avg_score < -0.1:
            sentiment_label = "CONCERNED"
        else:
            sentiment_label = "NEGATIVE"

        return sentiment_label

    except Exception as e:
        raise RuntimeError(f"Error during sentiment analysis: {e}")

# Example usage (for debugging purposes)
if __name__ == "__main__":
    sample_text = """
    I had a car accident last month. I've been feeling anxious and in pain since then.
    The physiotherapy sessions are helping, but the pain is still there sometimes.
    """
    try:
        result = analyze_sentiment(sample_text)
        print("Sentiment:\n", result)
    except Exception as e:
        print(f"Error: {e}")