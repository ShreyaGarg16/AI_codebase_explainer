from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from backend.services.loader import load_from_folder,load_from_github
from backend.services.chunker import chunk_code
from backend.services import state

router = APIRouter(prefix="/ingest", tags=["ingest"])



class IngestRequest(BaseModel):
    folder_path: Optional[str] = None
    github_url: Optional[str] = None

@router.post("")
def ingest_codebase(payload: IngestRequest):
    if payload.folder_path:
        files = load_from_folder(payload.folder_path)
    elif payload.github_url:
        files = load_from_github(payload.github_url)
    else:
        return {"error": "Provide folder_path or github_url"}

    chunks = chunk_code(files)

    state.CHUNKS = chunks
    state.INGESTED = True

    return {
        "status": "Ingested",
        "files": len(files),
        "chunks": len(chunks)
    }