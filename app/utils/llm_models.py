# import requests
# import logging
# from sentence_transformers import SentenceTransformer
# from app.utils.config import LLM_MODEL, EMBEDDING_MODEL, MAX_TOKENS, TEMPERATURE

# logger = logging.getLogger(__name__)

# # Embedding Model
# try:
#     embedding_model = SentenceTransformer(EMBEDDING_MODEL)
# except Exception as e:
#     logger.error(f"Embedding model loading error: {e}")
#     raise

# def get_embedding(text: str):
#     try:
#         return embedding_model.encode(text).tolist()
#     except Exception as e:
#         logger.error(f"Embedding generation error: {e}")
#         return []

# def generate_text(prompt: str, model: str = LLM_MODEL, max_tokens: int = MAX_TOKENS, temperature: float = TEMPERATURE):
#     """
#     Sends a request to Ollama HTTP API to generate text
#     """
#     try:
#         url = "http://localhost:11434/api/generate"
#         payload = {
#             "model": model,
#             "prompt": prompt,
#             "stream": False,
#             "temperature": temperature,
#             "num_predict": max_tokens
#         }
#         logger.debug(f"Sending request to Ollama: {payload['model']}")
#         response = requests.post(url, json=payload, timeout=60)
#         response.raise_for_status()
#         data = response.json()
#         return data.get("response") or data.get("completion") or "No response generated"
    
#     except requests.exceptions.ConnectionError:
#         logger.error("Cannot connect to Ollama. Make sure Ollama is running on localhost:11434")
#         return "Error: Cannot connect to LLM service"
#     except requests.exceptions.Timeout:
#         logger.error("Ollama request timeout")
#         return "Error: LLM request timeout"
#     except Exception as e:
#         logger.error(f"LLM generation error: {e}")
#         return f"Error generating response: {str(e)}"


import requests
import logging
from sentence_transformers import SentenceTransformer
from app.utils.config import LLM_MODEL, EMBEDDING_MODEL, MAX_TOKENS, TEMPERATURE

logger = logging.getLogger(__name__)

# Embedding Model
try:
    embedding_model = SentenceTransformer(EMBEDDING_MODEL)
except Exception as e:
    logger.error(f"Embedding model loading error: {e}")
    raise

def get_embedding(text: str):
    try:
        return embedding_model.encode(text).tolist()
    except Exception as e:
        logger.error(f"Embedding generation error: {e}")
        return []

def generate_text(prompt: str):
    """
    Sends a request to Ollama HTTP API to generate text
    """
    try:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False,
            "temperature": TEMPERATURE,
            "num_predict": MAX_TOKENS
        }
        logger.debug(f"Sending request to Ollama: {LLM_MODEL}")
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response generated")
    
    except requests.exceptions.ConnectionError:
        logger.error("Cannot connect to Ollama. Make sure Ollama is running on localhost:11434")
        return "Error: Cannot connect to LLM service"
    except requests.exceptions.Timeout:
        logger.error("Ollama request timeout")
        return "Error: LLM request timeout"
    except Exception as e:
        logger.error(f"LLM generation error: {e}")
        return f"Error generating response: {str(e)}"