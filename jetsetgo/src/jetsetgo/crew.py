# src/JetSetGo/crew.py
from crewai import Crew
from src.jetsetgo.config import agents
from src.jetsetgo.config import tasks

jetsetgo_crew = Crew(
    agents=agents,
    tasks=tasks,
    process="sequential",
    full_output=True,
    verbose=True,
    share_crew=False,
)