from crewai import Task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from keys import serper_api_key

# Initialize tools directly
scraper = ScrapeWebsiteTool()
serper = SerperDevTool(api_key=serper_api_key)

# Import agents after tools are defined
from Agents import travel_planner_ag, booking_agent

booking_task = Task(
    description=("""
    This task focuses on streamlining transportation (either flights or trains, whichever is the best) from {start_trip} on {start_date} to {destination} and return date will be next day from the stay. 
    Additionally, it includes finding suitable hotel accommodations in {destination} within the given budget of {Budget} for {people} people with a stay duration of {day} days.

    Key Considerations:
    - Prioritize the cheapest flight/train options while ensuring a balance between cost and convenience.
    - Find budget-friendly and well-rated hotels in {destination}.
    - Ensure all options are properly arranged in a structured format.
    - Provide direct booking links for flights, trains, and hotels.

    """),
    expected_output=f"""
    In markdown format: A structured report that categorizes available options under headings:
    - **Flights/Trains**: Cheapest available transportation options.
    - **Hotels**: Affordable and comfortable stay recommendations.
    
    Ensure that links to booking pages are included for all options.
    """,
    agent=booking_agent,
    tools=[scraper,serper],
)

travel_planner_task = Task(
    description = "streamline the places where user can visit including the main activity at {destination}.",
    agent = travel_planner_ag,
    expected_output = """
    In markdown format: A structured report that categorizes available options under headings:
    - **Flights/Trains**: Cheapest available transportation options with in the table having two rows.
    - **Hotels**: Affordable and comfortable stay recommendations with in the table having two rows.
    - **Schedule**: complete schedule from day to night with eating preferences with time stamps
    
    Ensure that links to booking pages are included for all options.
""",
    #output_file="Your_Plan.md"
)
