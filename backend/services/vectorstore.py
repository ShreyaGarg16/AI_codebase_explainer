"""import numpy as np
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

import faiss
import numpy as np
from backend.services.embeddings import embed_texts, embed_query

class VectorStore:
    def __init__(self, chunks):
        self.chunks = chunks
        self.texts = [c["text"] for c in chunks]

        embeddings = embed_texts(self.texts)
        self.vectors = np.array(embeddings).astype("float32")

        dim = self.vectors.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.vectors)

    def search(self, query, top_k=5):
        query_vec = np.array([embed_query(query)]).astype("float32")
        distances, indices = self.index.search(query_vec, top_k)
        return [self.chunks[i] for i in indices[0]]
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:
    def __init__(self, chunks):
        self.chunks = chunks
        self.texts = [c["text"] for c in chunks]

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000
        )
        self.vectors = self.vectorizer.fit_transform(self.texts)

    def search(self, query, top_k=5):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.vectors)[0]

        top_indices = scores.argsort()[::-1][:top_k]
        return [self.chunks[i] for i in top_indices]
