# AI Trip Planner FastAPI Backend

This FastAPI backend provides AI-powered travel planning services using CrewAI agents.

## Features

- RESTful API for trip planning
- Integration with CrewAI agents for intelligent travel recommendations
- Input validation and error handling
- CORS support for frontend integration
- Mock responses for development/testing

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Replace Placeholder Files**
   - Update `Agents.py` with your actual CrewAI agents
   - Update `task.py` with your actual CrewAI tasks
   - Ensure your agents and tasks are properly configured

4. **Run the Server**
   ```bash
   python main.py
   ```
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## API Endpoints

### POST /plan_trip
Generate a personalized travel plan.

**Request Body:**
```json
{
  "from_city": "New York",
  "destination": "Paris",
  "budget": 2000.0,
  "people": 2,
  "stay": 7,
  "start_date": "2024-06-15"
}
```

**Response:**
```json
{
  "travel_plan": "Detailed AI-generated travel plan...",
  "status": "success"
}
```

### GET /health
Check API health status.

### GET /
API information and available endpoints.

## Development Notes

- The application includes mock responses when CrewAI components are not available
- Replace the placeholder `Agents.py` and `task.py` with your actual implementations
- Configure your OpenAI and other API keys in the `.env` file
- The API supports CORS for frontend integration

## Production Deployment

1. Set appropriate CORS origins in production
2. Configure proper logging
3. Use environment variables for sensitive configuration
4. Consider using a production ASGI server like Gunicorn with Uvicorn workers

## Frontend Integration

The API is designed to work with the React frontend. Make sure to:
1. Update the frontend API URL to point to your backend
2. Handle loading states and errors appropriately
3. Test the complete flow from form submission to response display