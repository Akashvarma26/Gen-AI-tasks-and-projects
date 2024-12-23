# Importing libraries
from crewai import Task
from tools import get_yt_tool
from agents import blog_researcher,blog_writer
from config import *
# Research task
research_task = Task(
    description="Find relevant video content on the topic {topic}.",
    expected_output="A brief summary of video titles and descriptions.",
    tools=[get_yt_tool()],
    agent=blog_researcher
)

# writing task
writing_task=Task(
    description=(
        "Get info from yt channel on the topic {topic}."
    ),
    expected_output="Summarize the info from the yt channel video on the topic {topic} and create content for the blog.",
    tools=[get_yt_tool()],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)