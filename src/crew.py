"""
crew.py — Core orchestration script.
Loads agent personas and task instructions from config/ YAML files (Week 18 pattern).
Separates configuration from logic for scalability and testability.
"""
import yaml
from pathlib import Path
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()

CONFIG_DIR = Path(__file__).parent.parent / "config"


def _load_config(filename: str) -> dict:
    with open(CONFIG_DIR / filename, "r") as f:
        return yaml.safe_load(f)


def build_crew(topic: str) -> Crew:
    agents_cfg = _load_config("agents.yaml")
    tasks_cfg = _load_config("tasks.yaml")

    # --- Agents: personas loaded from config/agents.yaml ---
    researcher = Agent(
        role=agents_cfg["researcher"]["role"],
        goal=agents_cfg["researcher"]["goal"],
        backstory=agents_cfg["researcher"]["backstory"],
        verbose=True,
        allow_delegation=False,
    )

    writer = Agent(
        role=agents_cfg["writer"]["role"],
        goal=agents_cfg["writer"]["goal"],
        backstory=agents_cfg["writer"]["backstory"],
        verbose=True,
        allow_delegation=False,
    )

    # --- Tasks: instructions loaded from config/tasks.yaml ---
    research_task = Task(
        description=tasks_cfg["research_task"]["description"].format(topic=topic),
        expected_output=tasks_cfg["research_task"]["expected_output"],
        agent=researcher,
    )

    writing_task = Task(
        description=tasks_cfg["writing_task"]["description"].format(topic=topic),
        expected_output=tasks_cfg["writing_task"]["expected_output"],
        agent=writer,
        context=[research_task],
    )

    return Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )


def run_crew(topic: str) -> str:
    crew = build_crew(topic)
    return str(crew.kickoff())


if __name__ == "__main__":
    result = run_crew("AI Agentic Systems trends in 2025")
    print(result)
