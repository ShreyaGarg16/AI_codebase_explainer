from fastapi import FastAPI
from backend.api.health import router as health_router
from backend.api.ingest import router as ingest_router

app = FastAPI()
app.include_router(health_router)
app.include_router(ingest_router)

@app.get("/")
def root():
    return {"status": "Backend running"}
