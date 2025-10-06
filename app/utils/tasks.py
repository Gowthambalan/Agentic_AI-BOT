from crewai import Task

def create_research_task(query, agents):
    return Task(
        description=f"""Research: {query}
        
        IMPORTANT: 
        - First, search vector database
        - If vector DB has NO data, automatically delegate to WebAgent for web search
        - Provide the final answer from whichever source has information""",
        agent=agents[0],  # DataAgent starts
        expected_output="Final answer from either vector DB or web search",
        agents=agents  # Allow delegation between both agents
    )