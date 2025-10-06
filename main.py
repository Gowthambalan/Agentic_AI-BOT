# from app.agents.crew_orchestrator import run_query

# if __name__ == "__main__":
#     query = "SBI Bluechip Fund NAV 2015"
#     answer = run_query(query)
#     print("\nFinal Answer:\n", answer)


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
    return {"message": "CrewAI + RAG API is running 🚀"}
