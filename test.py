import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def test_serper():
    query = "who won the asia cup in 2025"
    
    print(f" Testing Serper API with: '{query}'")
    print(f" API Key: {SERPER_API_KEY[:10]}...")
    
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "q": query,
        "num": 5
    }
    
    try:
        # Use POST request to correct endpoint
        response = requests.post(
            "https://google.serper.dev/search",
            headers=headers,
            json=payload,
            timeout=10
        )
        
        print(f" Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f" Success! Found {len(data.get('organic', []))} results")
            
            if data.get('organic'):
                for i, result in enumerate(data['organic'][:3]):
                    print(f"\n--- Result {i+1} ---")
                    print(f"Title: {result.get('title', 'No title')}")
                    print(f"Snippet: {result.get('snippet', 'No snippet')}")
                    print(f"Link: {result.get('link', 'No link')}")
            else:
                print(" No organic results")
                print(f"Available keys: {data.keys()}")
                
        elif response.status_code == 401:
            print(" 401 Unauthorized - Invalid API Key")
        elif response.status_code == 429:
            print(" 429 Too Many Requests - API limit exceeded")
        else:
            print(f" Error {response.status_code}: {response.text}")
            
    except Exception as e:
        print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    test_serper()
