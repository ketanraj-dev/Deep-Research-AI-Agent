from agents import Agent,function_tool,ModelSettings
from models import get_model
from messenger import send_email,push
from dotenv import load_dotenv
import os


MODEL_NAME =  get_model("gemini", "gemini-3.1-flash-lite")
load_dotenv(override=True)
settings = ModelSettings(tool_choice="required")
USE_EMAIL = os.getenv("USE_EMAIL", "true").lower() == "true"

@function_tool
def send_email_tool(subject : str,text_body : str,html_body : str) -> str:
    """
    Send out an email with the given subject and body
    
    Args:
        subject: The subject of the email
        text_body: The body of the email as plain text
        html_body: The HTML body of the email
    """
    if USE_EMAIL:
        send_email(subject, text_body, html_body)
    else:
        push(f"Subject: {subject}\n\n{text_body}")
    return "Email sent successfully"

INSTRUCTION = """
You are an Email Formatting Agent.

You will receive a completed research report.

Your responsibilities:
- Create a professional HTML email.
- Generate a clear and descriptive subject line.
- Format the report with headings, paragraphs, bullet lists, tables (when appropriate), and proper spacing.
- Preserve all important information without changing its meaning.
- Ensure the email is readable across common email clients.
- Avoid unnecessary styling.
- Use semantic HTML.

After formatting the email, use the send_email_tool to send it.

Rewrite, shorten, or summarize the report if necessary for email readability.
"""

email_agent = Agent(name="Email Agent", instructions=INSTRUCTION, tools=[send_email_tool], model=MODEL_NAME, model_settings=settings)