from dotenv import load_dotenv
import os

load_dotenv()

LLM_MODEL = os.getenv("LLM_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH")
CHROMA_PERSIST = os.getenv("CHROMA_PERSIST", "True") == "True"
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1024))
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
