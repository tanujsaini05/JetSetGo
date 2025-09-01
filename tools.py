from crewai_tools import SerperDevTool,ScrapeWebsiteTool
from key import gooogle_api_key,serper_api_key
import os

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv('SERPER_API_KEY')
scraper = ScrapeWebsiteTool()
serper = SerperDevTool()