from re import search
from agents import Agent,WebSearchTool,ModelSettings
from dotenv import load_dotenv
import os
from models import get_model

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4o-mini"

INSTRUCTION = """
You are an expert Web Research Agent.

Your responsibility is to answer ONE search query using reliable web information.

For the given search query:

- Gather the most relevant and trustworthy information.
- Prefer authoritative and recent sources whenever possible.
- Remove duplicate or conflicting information.
- Focus only on information relevant to the search query.
- Produce a concise but information-rich summary.

Requirements:
- 2-3 well-structured paragraphs.
- Maximum 300 words.
- Preserve important facts, statistics, names, and dates.
- Do not include personal opinions.
- Do not speculate.
- Do not mention the search process.

Return only the summary.
"""

settings = ModelSettings(tool_choice="required")
tools = [WebSearchTool()]


search_agent = Agent(name="Search Agent",instructions=INSTRUCTION,tools=tools,model=MODEL_NAME)