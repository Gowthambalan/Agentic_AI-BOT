# from crewai import Crew
# from app.agents.crewai_agents import DataAgent, WebAgent, WriterAgent

# data_agent = DataAgent(name="DataAgent")
# web_agent = WebAgent(name="WebAgent")
# writer_agent = WriterAgent(name="WriterAgent")

# crew = Crew(agents=[data_agent, web_agent, writer_agent])

# def run_query(query):
#     data_result = data_agent.run(query)
#     if data_result:
#         final_input = data_result
#     else:
#         web_result = web_agent.run(query)
#         final_input = web_result

#     final_answer = writer_agent.run(final_input)
#     return final_answer

from crewai import Crew
from app.agents.crewai_agents import DataAgent, WebAgent, WriterAgent

data_agent = DataAgent(name="DataAgent")
web_agent = WebAgent(name="WebAgent")
writer_agent = WriterAgent(name="WriterAgent")

crew = Crew(agents=[data_agent, web_agent, writer_agent])

def run_query(query):
    data_result = data_agent.run(query)
    if data_result:
        final_input = data_result
    else:
        web_result = web_agent.run(query)
        final_input = web_result

    final_answer = writer_agent.run(final_input)
    return final_answer
