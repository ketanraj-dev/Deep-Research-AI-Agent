from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from config import PROVIDER

_clients = {
    provider : AsyncOpenAI(
        api_key = config["api_key"],
        base_url = config["base_url"]
    )
    for provider,config in PROVIDER.items()
}

def get_model(provider,model_name):
    if provider not in _clients:
        raise ValueError(f"Unknown provider: {provider}")
    return OpenAIChatCompletionsModel(
        model=model_name,
        openai_client=_clients[provider]
    )