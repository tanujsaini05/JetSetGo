# src/JetSetGo/crew.py
from crewai import Crew
from src.JetSetGo.config import agents
from src.JetSetGo.config import tasks

jetsetgo_crew = Crew(
    agents=agents,
    tasks=tasks,
    process="sequential",
    full_output=True,
    verbose=True,
    share_crew=False,
)