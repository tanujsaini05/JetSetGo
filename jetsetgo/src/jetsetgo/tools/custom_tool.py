# src/JetSetGo/tools/custom_tool.py
# Required by CrewAI structure — even if empty.
# Built-in tools (SerperDevTool, ScrapeWebsiteTool) are auto-imported via crewai[tools].
from crewai.tools import SerperDevTool, ScrapeWebsiteTool

# Optional: Define tool instances (used internally by CrewAI)
serper_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()