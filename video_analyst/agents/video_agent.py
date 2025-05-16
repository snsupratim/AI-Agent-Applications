from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import time

def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True,
    )

def analyze_video_with_agent(agent, video_path, user_query):
    uploaded_video = upload_file(video_path)
    while uploaded_video.state.name == "PROCESSING":
        time.sleep(1)
        uploaded_video = get_file(uploaded_video.name)

    prompt = (
        f"""
        Analyze the uploaded video for content and context.
        Respond to the following query using video insights and supplementary web research:
        {user_query}

        Provide a detailed, user-friendly, and actionable response.
        """
    )

    result = agent.run(prompt, videos=[uploaded_video])
    return result.content
