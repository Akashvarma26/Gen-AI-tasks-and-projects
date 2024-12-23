# Importing libraries
from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool to search within any Youtube channel's content the agent learns about during its execution
yt_tool = None

def get_yt_tool():
    global yt_tool
    if yt_tool is None:
        yt_tool = YoutubeChannelSearchTool(youtube_channel_handle="@codebasics")
    return yt_tool