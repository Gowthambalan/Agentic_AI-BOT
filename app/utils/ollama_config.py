from crewai import LLM
from app.utils.config import LLM_MODEL, TEMPERATURE, MAX_TOKENS

# Force CrewAI to use Ollama
OLLAMA_LLM = LLM(
    model=f"ollama/{LLM_MODEL}",
    base_url="http://localhost:11434",
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS
)