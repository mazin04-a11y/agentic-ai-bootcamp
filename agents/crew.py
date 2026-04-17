from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()


def create_research_agent() -> Agent:
    return Agent(
        role="Research Specialist",
        goal="Find accurate and up-to-date information on any topic",
        backstory=(
            "You are an expert researcher with years of experience gathering, "
            "analysing, and synthesising information from diverse sources."
        ),
        verbose=True,
        allow_delegation=False,
    )


def create_writer_agent() -> Agent:
    return Agent(
        role="Content Writer",
        goal="Produce clear, engaging, well-structured content based on research",
        backstory=(
            "You are a skilled writer who turns raw research into polished, "
            "readable output tailored to the intended audience."
        ),
        verbose=True,
        allow_delegation=False,
    )


def run_crew(topic: str) -> str:
    researcher = create_research_agent()
    writer = create_writer_agent()

    research_task = Task(
        description=f"Research the following topic thoroughly: {topic}",
        expected_output="A detailed summary of key facts, insights, and sources.",
        agent=researcher,
    )

    writing_task = Task(
        description=(
            f"Using the research provided, write a concise and engaging report on: {topic}"
        ),
        expected_output="A well-structured report (300–500 words) ready to publish.",
        agent=writer,
        context=[research_task],
    )

    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    return str(result)


if __name__ == "__main__":
    output = run_crew("AI agentic systems and their real-world applications")
    print(output)
