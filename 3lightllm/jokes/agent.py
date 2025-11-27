import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model= LiteLlm(
    model="openrouter/kwaipilot/kat-coder-pro:free"
,
    apikey=os.getenv("openrouter_api_key"),
)

def get_dad_jokes():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    return {"joke": random.choice(jokes)} 

root_agent = Agent(
    name="joke_agent", 
    model=model,
    description="A joke telling agent that tells dad jokes",
    instruction="You are a funny assistant that tells dad jokes to the user when they ask for one.",
    tools=[get_dad_jokes]
)