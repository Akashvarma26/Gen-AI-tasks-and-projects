# Importing libraries
from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,writing_task
from config import *



# Crew with enhanced configs
crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,writing_task],
    process=Process.sequential,
    memory=True,
    chache=True,
    max_rpm=100,
    share_crew=True
)

# Start task execution with feedback
result=crew.kickoff(inputs={"topic":"What is ML Ops?"})
print(result)