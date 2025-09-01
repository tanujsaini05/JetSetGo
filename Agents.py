from crewai import Agent,LLM
from crewai_tools import SerperDevTool,ScrapeWebsiteTool
#from key import gooogle_api_key
from tools import scraper,serper
import google.generativeai as genai
import os
from crewai_tools import SerperDevTool, ScrapeWebsiteTool


scraper = ScrapeWebsiteTool()
serper = SerperDevTool()
# llm = LLM(
#     model="gemini/gemini-1.5-flash",
#     temperature=0.7,
#     #vertex_credentials=vertex_credentials_json
#     api_key=gooogle_api_key
# )

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#genai.configure(api_key=GOOGLE_API_KEY)

llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7,
    api_key=GOOGLE_API_KEY
)

booking_agent = Agent(
    role = "Booking Specialist",
    goal = "Streamline a flights or trains (which ever will be the best)with in the budget. ",
    backstory = ("""You are skilled in finding the best deals and securing bookings quickly at cheapest."""),
    memory = True,
    allow_deligation = True,
    verbose = True,
    tools = [scraper,serper],
    llm = llm)

travel_planner_ag = Agent(
    role = "Travel Planner",
    goal = "Schedule the complete plan from day to night.",
    backstory = ("An expert in travel planning who knows the best destinations for every type of traveler."),
    tools = [scraper,serper],
    memory = True,
    allow_deligation = True,
    llm = llm ,verbose = True
)

