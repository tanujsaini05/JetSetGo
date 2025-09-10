from crewai import Agent,LLM
from keys import gooogle_api_key, serper_api_key
import google.generativeai as genai
import os
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

# Initialize tools directly here to avoid import issues
scraper = ScrapeWebsiteTool()
serper = SerperDevTool(api_key=serper_api_key)

# Use the API key from keys.py
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7,
    api_key=gooogle_api_key
)

booking_agent = Agent(
    role = "Booking Specialist",
    goal = "Streamline a flights or trains (which ever will be the best)with in the budget. ",
    backstory = ("""You are skilled in finding the best deals and securing bookings quickly at cheapest."""),
    memory = True,
    allow_delegation = True,
    verbose = True,
    tools = [scraper,serper],
    llm = llm)

travel_planner_ag = Agent(
    role = "Travel Planner",
    goal = "Schedule the complete plan from day to night.",
    backstory = ("An expert in travel planning who knows the best destinations for every type of traveler."),
    tools = [scraper,serper],
    memory = True,
    allow_delegation = True,
    llm = llm ,verbose = True
)

