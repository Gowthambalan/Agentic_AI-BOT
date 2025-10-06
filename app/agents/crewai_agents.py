# from crewai import Agent
# from app.utils.rag import search_vector_db
# from app.utils.web_search import search_web
# from app.utils.llm_models import generate_text

# class DataAgent(Agent):
#     def run(self, query):
#         result = search_vector_db(query)
#         if result:
#             return generate_text(result)
#         return None

# class WebAgent(Agent):
#     def run(self, query):
#         result = search_web(query)
#         if result:
#             return generate_text(result)
#         return None

# class WriterAgent(Agent):
#     def run(self, *inputs):
#         combined = " ".join(filter(None, inputs))
#         return generate_text(combined)


from crewai import Agent
from app.utils.rag import search_vector_db
from app.utils.web_search import search_web
from app.utils.llm_models import generate_text

class DataAgent(Agent):
    def __init__(self, **kwargs):
        # Provide default values for required fields
        defaults = {
            'role': 'Data Analysis Specialist',
            'goal': 'Extract insights and analyze data from various sources', 
            'backstory': 'You are an expert data analyst with years of experience in processing and analyzing complex datasets.',
            'allow_delegation': False
        }
        # Merge defaults with any provided kwargs
        defaults.update(kwargs)
        super().__init__(**defaults)
    
    def run(self, query):
        result = search_vector_db(query)
        if result:
            return generate_text(result)
        return None

class WebAgent(Agent):
    def __init__(self, **kwargs):
        defaults = {
            'role': 'Web Research Specialist',
            'goal': 'Gather and synthesize information from web sources',
            'backstory': 'You are a skilled web researcher who can find relevant information from various online sources.',
            'allow_delegation': False
        }
        defaults.update(kwargs)
        super().__init__(**defaults)
    
    def run(self, query):
        result = search_web(query)
        if result:
            return generate_text(result)
        return None

class WriterAgent(Agent):
    def __init__(self, **kwargs):
        defaults = {
            'role': 'Content Writer and Editor',
            'goal': 'Create well-structured and engaging content based on research findings',
            'backstory': 'You are a professional writer who excels at turning complex information into clear, engaging content.',
            'allow_delegation': False
        }
        defaults.update(kwargs)
        super().__init__(**defaults)
    
    def run(self, *inputs):
        combined = " ".join(filter(None, inputs))
        return generate_text(combined)