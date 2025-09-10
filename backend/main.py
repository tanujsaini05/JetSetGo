from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date
from typing import Optional
import logging

# Import your CrewAI components
try:
    from crewai import Crew, Process
    from task import booking_task, travel_planner_task
    from Agents import booking_agent, travel_planner_ag
    CREWAI_AVAILABLE = True
except ImportError as e:
    logging.warning(f"CrewAI imports failed: {e}. Using mock responses for development.")
    booking_agent = None
    travel_planner_ag = None
    booking_task = None
    travel_planner_task = None
    CREWAI_AVAILABLE = False

# Initialize FastAPI app
app = FastAPI(
    title="AI Trip Planner API",
    description="AI-powered travel planning service using CrewAI agents",
    version="1.0.0"
)

# Add CORS middleware to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model matching your frontend
class TripRequest(BaseModel):
    from_city: str
    destination: str
    budget: float
    people: int
    stay: int
    start_date: str  # format: YYYY-MM-DD

# Define response model
class TripResponse(BaseModel):
    travel_plan: str
    status: str = "success"

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "🌍 Welcome to AI Trip Planner API",
        "description": "AI-powered travel planning service",
        "endpoints": {
            "plan_trip": "POST /plan_trip - Generate a travel plan",
            "health": "GET /health - Check API health",
            "docs": "GET /docs - API documentation"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "AI Trip Planner API"}

@app.post("/plan_trip", response_model=TripResponse)
async def plan_trip(request: TripRequest):
    """
    Generate a personalized travel plan using AI agents
    
    Args:
        request: TripRequest containing travel details
        
    Returns:
        TripResponse with generated travel plan
    """
    try:
        # Validate input data
        if not request.from_city.strip():
            raise HTTPException(status_code=400, detail="From city is required")
        if not request.destination.strip():
            raise HTTPException(status_code=400, detail="Destination is required")
        if request.budget <= 0:
            raise HTTPException(status_code=400, detail="Budget must be greater than 0")
        if request.people <= 0:
            raise HTTPException(status_code=400, detail="Number of people must be greater than 0")
        if request.stay <= 0:
            raise HTTPException(status_code=400, detail="Stay duration must be greater than 0")
        
        # Validate date format
        try:
            date.fromisoformat(request.start_date)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
        
        # Check if CrewAI components are available
        if not CREWAI_AVAILABLE:
            # Return mock response for development/testing
            mock_plan = generate_mock_travel_plan(request)
            return TripResponse(travel_plan=mock_plan)
        
        # Create and run CrewAI crew
        crew = Crew(
            agents=[booking_agent, travel_planner_ag],
            tasks=[booking_task, travel_planner_task],
            process=Process.sequential,
            full_output=True,
            share_crew=False,
            verbose=True
        )
        
        # Execute the crew with input parameters
        result = crew.kickoff(inputs={
            "start_trip": request.from_city,
            "destination": request.destination,
            "Budget": request.budget,
            "people": request.people,
            "day": request.stay,
            "start_date": request.start_date
        })
        
        # Convert result to string
        travel_plan = str(result)
        
        return TripResponse(travel_plan=travel_plan)
        
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error generating travel plan: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to generate travel plan: {str(e)}"
        )

def generate_mock_travel_plan(request: TripRequest) -> str:
    """Generate a mock travel plan for development/testing"""
    return f"""
🌍 **AI-Powered Travel Plan**

**Trip Overview:**
• From: {request.from_city}
• To: {request.destination}
• Duration: {request.stay} days
• Travelers: {request.people} people
• Budget: ${request.budget:,.2f}
• Departure: {request.start_date}

**Day-by-Day Itinerary:**

**Day 1: Arrival & City Exploration**
• Morning: Arrive in {request.destination}
• Afternoon: Check into accommodation
• Evening: Explore local neighborhood and try authentic cuisine

**Day 2-{request.stay-1}: Main Activities**
• Visit top attractions and landmarks
• Experience local culture and traditions
• Enjoy recommended restaurants and cafes
• Optional day trips to nearby attractions

**Day {request.stay}: Departure**
• Morning: Last-minute shopping or sightseeing
• Afternoon: Check out and head to airport/station

**Budget Breakdown:**
• Accommodation: ${request.budget * 0.4:,.2f} (40%)
• Food & Dining: ${request.budget * 0.3:,.2f} (30%)
• Activities & Tours: ${request.budget * 0.2:,.2f} (20%)
• Transportation: ${request.budget * 0.1:,.2f} (10%)

**Travel Tips:**
• Book accommodations in advance for better rates
• Try local street food for authentic experiences
• Use public transportation to save money
• Keep important documents secure

**Note:** This is a mock response. Connect your CrewAI agents for personalized AI-generated plans.
    """.strip()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)