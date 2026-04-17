from crewai.tools import BaseTool
from pydantic import Field


class EchoTool(BaseTool):
    """Placeholder custom tool — replace with your own logic."""

    name: str = "Echo Tool"
    description: str = "Returns the input text unchanged. Use as a template for custom tools."

    def _run(self, text: str) -> str:
        return f"Echo: {text}"
