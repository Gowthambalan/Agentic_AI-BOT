import requests
from app.utils.config import SERPER_API_KEY

def search_web(query):
    headers = {"X-API-KEY": SERPER_API_KEY}
    response = requests.get(f"https://api.serper.dev/search?q={query}", headers=headers)
    data = response.json()
    snippets = [item["snippet"] for item in data.get("results", [])]
    return " ".join(snippets)
