from google.adk.agents import Agent
from google.adk.tools import google_search 

# def get_current_time() -> dict :
#     "get the current date and time"
#     from datetime import datetime
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }
root_agent = Agent (
    name="tool_agent",
    model="openrouter/kwaipilot/kat-coder-pro:free",
    description="Tool agent",
    instruction="you are an assistant that can use tools to help the user- google search",
   # tools=[get_current_time, google_search],-->work
    tools=[google_search]
    #tools=[get_current_time]
)
