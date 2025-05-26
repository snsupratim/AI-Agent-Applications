from langchain_community.tools.tavily_search import TavilySearchResults

def get_tools(enabled: bool):
    return [TavilySearchResults(max_results=2)] if enabled else []
