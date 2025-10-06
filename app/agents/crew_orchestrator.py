# from crewai import Crew, Process
# from app.agents.crewai_agents import DataAgent, WebAgent, WriterAgent
# from app.utils.tasks import create_research_task, create_writing_task
# from app.utils.llm_models import generate_text
# import logging

# logging.basicConfig(level=logging.INFO)

# data_agent = DataAgent()
# web_agent = WebAgent()
# writer_agent = WriterAgent()

# def run_query(query: str):
#     """
#     Executes the CrewAI pipeline: vector DB + web search + writing using Ollama
#     """
#     try:
#         # Create tasks
#         research_task = create_research_task(query, [data_agent, web_agent])
#         writing_task = create_writing_task(query, [writer_agent])

#         # Create Crew with custom LLM client
#         crew = Crew(
#             agents=[data_agent, web_agent, writer_agent],
#             tasks=[research_task, writing_task],
#             process=Process.sequential,
#             verbose=True,
#             llm_client=generate_text  # Force Ollama usage
#         )

#         # Execute the workflow
#         result = crew.kickoff()
#         return result
#     except Exception as e:
#         logging.error(f"Error in crew orchestration: {e}")
#         return f"Error processing query: {str(e)}"

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