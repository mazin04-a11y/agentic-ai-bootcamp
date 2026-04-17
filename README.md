# Agentic AI Bootcamp — CrewAI Service

A professional-grade multi-agent AI service built following the Week 18 "Blueprint Blue" architecture standards from the 20-week AI Agentic Systems bootcamp.

## Architecture (Week 18 Pattern)

```
agentic-ai-bootcamp/
├── src/
│   ├── crew.py          # Core orchestration — assembles agents + tasks into crew
│   ├── agents/          # Modular agent definitions
│   ├── tasks/           # Task definitions
│   └── tools/           # Custom utility tools
├── config/
│   ├── agents.yaml      # Agent personas (role, goal, backstory)
│   └── tasks.yaml       # Task instructions (description, expected_output)
├── tests/               # Unit + integration tests
├── app/
│   ├── streamlit_app.py # Streamlit UI frontend
│   └── main.py          # FastAPI backend
├── .env.example         # Environment variable template
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml   # Jenkins + app services
└── Jenkinsfile          # CI/CD pipeline
```

## Key Design Principles

- **Separation of Concerns** — config isolated from logic (YAML configs)
- **Modular Structure** — agents, tasks, tools in separate folders
- **Immune System** — try/except/finally error handling on critical steps
- **ID Badge Protocol** — all API keys via `.env`, never hardcoded

## Setup

1. Copy `.env.example` to `.env` and fill in your API keys:
   ```
   ANTHROPIC_API_KEY=your_key
   OPENAI_API_KEY=your_key
   SERPER_API_KEY=your_key
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the crew locally:
   ```bash
   python src/crew.py
   ```

4. Run the Streamlit UI:
   ```bash
   streamlit run app/streamlit_app.py
   ```

5. Run tests:
   ```bash
   pytest
   ```

## CI/CD

Jenkins runs inside Docker. Start with:
```bash
docker compose up -d
```
Jenkins available at: http://localhost:8080

The Jenkinsfile pipeline: Install → Test → Docker Build → Push to GitHub → Streamlit Cloud redeploys.

## Stack

| Layer | Technology |
|-------|-----------|
| Agent Framework | CrewAI |
| UI | Streamlit |
| API | FastAPI |
| CI/CD | Docker + Jenkins |
| Deployment | Streamlit Cloud |
