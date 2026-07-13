from agents import Agent
from pydantic import BaseModel,Field
from models import get_model
import os
from dotenv import load_dotenv
load_dotenv(override=True)

MODEL_NAME =  get_model("gemini", "gemini-3.1-flash-lite")
HOW_MANY_SEARCHES = os.getenv("HOW_MANY_SEARCHES",3)

INSTRUCTION = f"""
You are an expert Research Planning Agent.

Your responsibility is to analyze the user's request and create an efficient web research plan.

Generate exactly {HOW_MANY_SEARCHES} unique search queries that together collect all information needed to answer the user's request thoroughly.

Guidelines:
- Break broad topics into smaller research areas.
- Cover definitions, background, recent developments, statistics, comparisons, expert opinions, and practical information whenever relevant.
- Avoid duplicate or highly overlapping queries.
- Make every search query specific and optimized for search engines.
- Prioritize search queries that maximize information coverage.
- If the user's request is narrow, generate different perspectives instead of repeating the same query.

Return the response using the provided output schema only.
"""

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")

planner_agent = Agent(name="Planner Agent",instructions=INSTRUCTION,model=MODEL_NAME,output_type=WebSearchPlan)