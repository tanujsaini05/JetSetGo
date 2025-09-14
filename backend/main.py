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

    # ⚠️ IMPORTANT: Keys MUST match what's used in task descriptions!
    result = crew_.kickoff(inputs={
        "origin": request.from_city,      # <-- Match task's {origin}
        "destination": request.destination,
        "budget": request.budget,         # <-- NOT "Budget"
        "num_people": request.people,     # <-- NOT "people"
        "days": request.stay,             # <-- NOT "day"
        "start_date": request.start_date
    })

    # Return clean response
    return {
        "travel_plan": result.final_output.raw_output if hasattr(result.final_output, 'raw_output') else str(result.final_output),
        "success": True
    }

@app.get("/")
def home():
    return {"message": "Welcome to AI Trip Planner API 🚀. Go to /docs to try it out."}
