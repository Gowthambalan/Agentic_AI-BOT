# from sentence_transformers import SentenceTransformer
# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch
# from app.utils.config import LLM_MODEL, EMBEDDING_MODEL, MAX_TOKENS

# embedding_model = SentenceTransformer(EMBEDDING_MODEL)

# tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
# llm_model = AutoModelForCausalLM.from_pretrained(
#     LLM_MODEL,
#     device_map="auto",
#     torch_dtype=torch.float16
# )

# def generate_text(prompt, max_tokens=MAX_TOKENS):
#     inputs = tokenizer(prompt, return_tensors="pt").to(llm_model.device)
#     outputs = llm_model.generate(**inputs, max_new_tokens=max_tokens)
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)


import requests
import json
from sentence_transformers import SentenceTransformer
from app.utils.config import LLM_MODEL, EMBEDDING_MODEL, MAX_TOKENS, TEMPERATURE

# ---------------- Embedding Model ----------------
embedding_model = SentenceTransformer(EMBEDDING_MODEL)

def get_embedding(text: str):
    """Get embedding vector using SentenceTransformer."""
    return embedding_model.encode(text).tolist()

# ---------------- LLM (Ollama) ----------------
def generate_text(prompt: str, model: str = LLM_MODEL, max_tokens: int = MAX_TOKENS, temperature: float = TEMPERATURE):
    """
    Generate text using Ollama (deepseek-r1:8b in .env).
    Uses stream=False to simplify response handling.
    """
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False,  # Change to False to get full response at once
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens
        }
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()  # Raises HTTPError if 4xx/5xx

    data = response.json()
    # Ollama returns either "response" or "completion" depending on version
    return data.get("response") or data.get("completion")
