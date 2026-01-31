from sklearn.feature_extraction.text import TfidfVectorizer

def get_embedding_model():
    """
    Returns a TF-IDF vectorizer for local embeddings.
    Stable, fast, and offline.
    """
    vectorizer = TfidfVectorizer(
        max_features=5000,
        stop_words="english"
    )
    return vectorizer
