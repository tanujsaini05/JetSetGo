from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew, Process
from Agents import booking_agent, travel_planner_ag
from task import booking_task, travel_planner_task

# Initialize FastAPI app
app = FastAPI(title="AI Trip Planner", version="1.0")

# Define request model
class TripRequest(BaseModel):
    from_city: str
    destination: str
    budget: float
    people: int
    stay: int
    start_date: str  # format: YYYY-MM-DD

@app.post("/plan_trip")
async def plan_trip(request: TripRequest):
    # Create crew
    crew_ = Crew(
        agents=[booking_agent, travel_planner_ag],
        tasks=[booking_task, travel_planner_task],
        process=Process.sequential,
        full_output=True,
        share_crew=False,
        verbose=True
    )

    # Run agents
    result = crew_.kickoff(inputs={
        "start_trip": request.from_city,
        "destination": request.destination,
        "Budget": request.budget,
        "people": request.people,
        "day": request.stay,
        "start_date": request.start_date
    })

    return {"travel_plan": str(result)}

@app.get("/")
def home():
    return {"message": "Welcome to AI Trip Planner API 🚀. Go to /docs to try it out."}
