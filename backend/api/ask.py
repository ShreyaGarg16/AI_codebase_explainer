from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.loader import load_codebase
from backend.services.chunker import chunk_code
from backend.services.embeddings import get_embeddings
from backend.services.vectorstore import create_vector_store
from backend.services.rag import ask_question

router = APIRouter()

class AskRequest(BaseModel):
    repo_path: str
    question: str

@router.post("/ask")
def ask_codebase(data: AskRequest):
    # 1. Load code
    files = load_codebase(data.repo_path)

    # 2. Chunk code
    chunks = chunk_code(files)

    # 3. Create embeddings
    embeddings = get_embeddings()

    # 4. Vector store
    vector_store = create_vector_store(chunks, embeddings)

    # 5. Ask question via RAG
    answer = ask_question(vector_store, data.question)

    return {
        "question": data.question,
        "answer": answer
    }
