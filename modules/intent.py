import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load intent model (small and efficient)
intent_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define possible intents
INTENTS = [
    "Seeking reassurance",
    "Reporting symptoms",
    "Expressing concern",
    "Requesting treatment",
    "Discussing recovery"
]

def detect_intent(text):
    """
    Detects the user's intent based on semantic similarity.

    Args:
        text (str): The input text to analyze for intent.

    Returns:
        str: Detected intent based on highest similarity score.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input text must be a non-empty string.")

    try:
        # Generate embeddings for known intents and input text
        intent_embeddings = intent_model.encode(INTENTS)
        text_embedding = intent_model.encode([text])

        # Compute cosine similarity between input text and intents
        similarity_scores = cosine_similarity(text_embedding, intent_embeddings)[0]
        best_match_index = np.argmax(similarity_scores)
        best_intent = INTENTS[best_match_index]

        return best_intent

    except Exception as e:
        # Catch any encoding or similarity calculation errors
        raise RuntimeError(f"Intent detection failed: {e}")

# Example usage (for testing purposes)
if __name__ == "__main__":
    sample_text = "I'm experiencing a lot of back pain after my car accident."
    
    try:
        detected_intent = detect_intent(sample_text)
        print(f"Detected Intent: {detected_intent}")
    except Exception as e:
        print(f"Error: {e}")