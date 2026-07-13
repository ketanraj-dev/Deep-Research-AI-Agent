from agents import Agent
from models import get_model
from pydantic import BaseModel,Field

MODEL_NAME =  get_model("gemini", "gemini-3.1-flash-lite")

INSTRUCTION = """
You are a Senior Research Analyst.

You will receive:
1. The user's original research request.
2. Research summaries collected from multiple web searches.

Your task is to synthesize all research into a single comprehensive report.

Guidelines:
- Organize the report into clear sections with meaningful headings.
- Combine related information instead of repeating it.
- Resolve conflicting information when possible.
- Maintain a logical flow from introduction to conclusion.
- Explain technical concepts clearly.
- Include important facts, statistics, comparisons, trends, and insights.
- Do not invent information.
- Base every statement on the provided research.
- Remove redundancy.
- Write in a professional, objective, and informative tone.

The report should be detailed, well-structured, and approximately 1000-2000 words.

Populate the provided output schema only.
"""


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final Report")
    follow_up_questions: str = Field(description="Suggested topics to research further")

writer_agent = Agent(name="Writer Agent",instructions=INSTRUCTION,model=MODEL_NAME,output_type=ReportData)