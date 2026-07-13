from dotenv import load_dotenv
import os
from openai import AsyncOpenAI, api_key, base_url

load_dotenv(override=True)



GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
OPENAI_BASE_URL = "https://api.openai.com/v1/"

PROVIDER = {
    "openai" : {
        "api_key" : os.getenv("OPENAI_API_KEY"),
        "base_url" : "https://api.openai.com/v1/",
    },
    "gemini" : {
        "api_key" : os.getenv("GOOGLE_API_KEY"),
        "base_url" : "https://generativelanguage.googleapis.com/v1beta/openai/"
    },
    "deepseek" : {
        "api_key" : os.getenv("DEEPSEEK_API_KEY"),
        "base_url" : "https://api.deepseek.com"
    }
}
