from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from keys import serper_api_key

# Initialize tools with API keys
def get_scraper_tool():
    return ScrapeWebsiteTool()

def get_serper_tool():
    return SerperDevTool(api_key=serper_api_key)

# Create tool instances
scraper = get_scraper_tool()
serper = get_serper_tool()