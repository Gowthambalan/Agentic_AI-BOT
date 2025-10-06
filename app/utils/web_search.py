import requests
from app.utils.config import SERPER_API_KEY
import logging

logger = logging.getLogger(__name__)

def search_web(query):
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    
    logger.info(f"🌐 Web search for: {query}")
    
    try:
        # Use POST request with JSON body (correct Serper API format)
        payload = {
            "q": query,
            "num": 10  # Number of results
        }
        
        response = requests.post(
            "https://google.serper.dev/search",  # ✅ CORRECT ENDPOINT
            headers=headers,
            json=payload,
            timeout=15
        )
        
        logger.info(f"📊 HTTP Status: {response.status_code}")
        
        if response.status_code != 200:
            logger.error(f"❌ API Error {response.status_code}: {response.text}")
            return None
            
        data = response.json()
        logger.info(f"📄 Found {len(data.get('organic', []))} organic results")
        
        # Extract snippets from organic results
        snippets = [item["snippet"] for item in data.get("organic", []) if "snippet" in item]
        
        if snippets:
            result_text = " ".join(snippets)
            logger.info(f"✅ Web search successful: {len(result_text)} chars")
            return result_text
        else:
            logger.warning("❌ No snippets in results")
            return None
            
    except Exception as e:
        logger.error(f"❌ Web search failed: {e}")
        return None