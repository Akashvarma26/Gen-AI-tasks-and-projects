# Importing Libraries
from config import *
from crewai import Agent, LLM
from tools import get_yt_tool


# LLM Config
llm=LLM(model="gpt-4o-mini",
        temperature=0.7,
        )
# Create a senior blog content researcher Agent
blog_researcher=Agent(
    role="Blog researcher from youtube videos",
    goal="Get the revelant video content for the topic {topic} from Yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding Computer Science related Technologies particulary in cloud computing, AI and Web development,etc and providing suggestions."
    ),
    tools=[get_yt_tool()],
    allow_delegation=True,  # Allows other agents to use this Agent's response
    llm=llm
)

# Create a senior blog writer Agent who will access response from researcher
blog_writer=Agent(
    role="Blog writer from youtube videos",
    goal="Narrate and write compelling tech content about the video {topic} from yt channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives tyhat cativate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[get_yt_tool()],
    allow_delegation=False,
    llm=llm
)
