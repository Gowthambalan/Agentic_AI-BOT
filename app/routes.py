from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.crew_orchestrator import run_query

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/ask")
def ask_question(req: QueryRequest):
    try:
        answer = run_query(req.query)
    except Exception as e:
        answer = "Sorry, could not generate an answer."
    return {"query": req.query, "answer": answer}
