from crewai import Agent
from app.utils.rag import search_vector_db
from app.utils.web_search import search_web
from app.utils.llm_models import generate_text
from app.utils.ollama_config import OLLAMA_LLM
import logging

logger = logging.getLogger(__name__)

class DataAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Data Analysis Specialist',
            goal='Extract insights and analyze data from vector database. If no data found, delegate to web search.',
            backstory='You are an expert data analyst who checks vector database first, then delegates to web research if needed.',
            allow_delegation=True,  # ✅ Enable delegation
            verbose=True,
            llm=OLLAMA_LLM
        )

    def run(self, query):
        try:
            results = search_vector_db(query)
            if results and results.get('documents') and results['documents'][0]:
                context = "\n".join(results['documents'][0])
                prompt = f"Based on the vector database context, answer: {query}\n\nContext: {context}"
                answer = generate_text(prompt)
                return f"📊 FROM VECTOR DB:\n{answer}"
            else:
                # Return special signal to trigger web search
                return "NO_DATA_FOUND"
        except Exception as e:
            logger.error(f"DataAgent error: {e}")
            return "NO_DATA_FOUND"

class WebAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Web Research Specialist',
            goal='Gather and synthesize information from web sources when vector DB has no data',
            backstory='You are a skilled web researcher who finds relevant information from various online sources.',
            allow_delegation=False,
            verbose=True,
            llm=OLLAMA_LLM
        )

    def run(self, query):
        try:
            logger.info(f"🌐 WebAgent searching for: {query}")
            results = search_web(query)
            
            if results and len(results) > 10:
                prompt = f"""Provide a clear, direct answer to this query: {query}
                
                Web Search Results: {results}
                
                Answer directly based on the web information:"""
                print("wdghvhsdvhs")
                answer = generate_text(prompt)
                return f"🌐 FROM WEB SEARCH:\n{answer}"
            else:
                return "❌ No relevant web results found."
        except Exception as e:
            logger.error(f"WebAgent error: {e}")
            return f"Error in WebAgent: {str(e)}"