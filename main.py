from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="CrewAI RAG System",
    description="FastAPI + CrewAI + Ollama + ChromaDB",
    version="1.0.0"
)

# Include routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "CrewAI + RAG API is running "}
