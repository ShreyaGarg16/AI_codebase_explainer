from fastapi import APIRouter
from pydantic import BaseModel

from backend.services import state
from backend.services.rag import answer_question

router = APIRouter(prefix="/ask", tags=["ask"])


class AskRequest(BaseModel):
    question: str


@router.post("")

def ask_codebase(payload: AskRequest):
    if not state.INGESTED:
        return {"error": "Please ingest a repository first"}

    return answer_question(state.CHUNKS, payload.question)

