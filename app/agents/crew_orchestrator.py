import logging
from app.utils.rag import search_vector_db
from app.utils.web_search import search_web
from app.utils.llm_models import generate_text

logging.basicConfig(level=logging.INFO)

def run_query(query: str):
    """
    Direct pipeline: Vector DB → Web Search (automatic fallback)
    """
    try:
        logging.info(f"🔍 Processing: {query}")
        
        # Step 1: Try Vector DB First
        vector_results = search_vector_db(query)
        
        if vector_results and vector_results.get('documents') and vector_results['documents'][0]:
            documents = vector_results['documents'][0]
            context = "\n".join(documents)
            prompt = f"Answer: {query}\n\nContext: {context}"
            vector_answer = generate_text(prompt)
            logging.info("✅ Answer from Vector DB")
            return f"📊 FROM VECTOR DATABASE:\n{vector_answer}"
        
        # Step 2: Automatic fallback to Web Search
        logging.info("📡 No Vector DB data, switching to web search...")
        web_results = search_web(query)
        
        if web_results and len(web_results) > 10:
            prompt = f"""Answer this query based on recent web information: {query}
            
            Web Search Results: {web_results}
            
            Provide a direct answer:"""
            
            web_answer = generate_text(prompt)
            logging.info("✅ Answer from Web Search")
            return f"🌐 FROM WEB SEARCH:\n{web_answer}"
        else:
            return "❌ No information found in vector database or web search."
            
    except Exception as e:
        logging.error(f"Error: {e}")
        return f"Error processing query: {str(e)}"