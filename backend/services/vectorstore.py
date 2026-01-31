import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from backend.services.embeddings import get_embedding_model


class VectorStore:
    def __init__(self, chunks):
        self.chunks = chunks
        self.texts = [c["text"] for c in chunks]

        self.vectorizer = get_embedding_model()
        self.vectors = self.vectorizer.fit_transform(self.texts)

    def search(self, query, top_k=5):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.vectors)[0]

        top_indices = np.argsort(scores)[::-1][:top_k]

        return [self.chunks[i] for i in top_indices]
