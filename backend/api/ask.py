from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.loader import load_codebase
from backend.services.chunker import chunk_code
from backend.services.rag import answer_question

router = APIRouter(prefix="/ask", tags=["ask"])


class AskRequest(BaseModel):
    folder_path: str
    question: str


@router.post("")
def ask_codebase(payload: AskRequest):
    files = load_codebase(payload.folder_path)
    chunks = chunk_code(files)

    answer = answer_question(chunks, payload.question)

    return {
        "question": payload.question,
        "answer": answer
    }
