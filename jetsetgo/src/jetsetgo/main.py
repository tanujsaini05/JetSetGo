# src/JetSetGo/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from src.jetsetgo.crew import jetsetgo_crew

app = FastAPI(title="JetSetGo AI Trip Planner", version="1.0")

class TripRequest(BaseModel):
    origin: str
    destination: str
    budget: float
    num_people: int
    days: int
    start_date: str

@app.post("/plan_trip")
async def plan_trip(request: TripRequest):
    result = jetsetgo_crew.kickoff(inputs={
        "origin": request.origin,
        "destination": request.destination,
        "budget": request.budget,
        "num_people": request.num_people,
        "days": request.days,
        "start_date": request.start_date
    })

    return {
        "travel_plan": result.final_output.raw_output if hasattr(result.final_output, 'raw_output') else str(result.final_output),
        "success": True
    }

@app.get("/")
def home():
    return {"message": "Welcome to JetSetGo AI Trip Planner 🚀. Go to /docs to try it out."}