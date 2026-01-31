from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class IngestRequest(BaseModel):
    github_url: Optional[str] = None
    zip_name: Optional[str] = None

@router.post("/ingest")
def ingest_repo(data: IngestRequest):
    if not data.github_url and not data.zip_name:
        return {"error": "Provide github_url or zip_name"}

    return {
        "message": "Ingest request received",
        "github_url": data.github_url,
        "zip_name": data.zip_name
    }
