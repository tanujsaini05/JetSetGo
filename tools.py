from crewai_tools import ScrapeWebsiteTool
# from key import gooogle_api_key,serper_api_key
import os

GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")
SERPER_API_KEY = os.getenv('SERPER_API_KEY')
scraper = ScrapeWebsiteTool()
# serper = SerperDevTool()