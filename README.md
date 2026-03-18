# Google ADK Agent Collection

A progressive series of AI agents built with **Google Agent Development Kit (ADK)** — from basic reasoning agents to multi-tool systems with memory, structured outputs, and session management.

## Agents in this repo

| Folder | Agent | What it does |
|---|---|---|
| `1basic_agent` | Basic Agent | Simple conversational agent — foundation of ADK, tool-free reasoning |
| `2tool_agent` | Tool Agent | Agent with external tool access — web search, function calling |
| `3lightllm` | LightLLM Agent | Lightweight LLM integration — optimised inference patterns |
| `4structured_outputs` | Structured Output Agent | Forces JSON/structured responses — critical for production pipelines |
| `5sessions` | Session Agent | Persistent memory across turns — stateful multi-turn conversations |

## Tech stack

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![Google ADK](https://img.shields.io/badge/Google-ADK-orange?style=flat&logo=google)
![Generative AI](https://img.shields.io/badge/GenAI-Agent%20Framework-green?style=flat)

- **Framework:** Google Agent Development Kit (ADK)
- **Language:** Python 3.10+
- **LLM:** Google Gemini (via ADK)
- **Patterns:** Tool use, structured outputs, session memory, multi-step reasoning

## Setup

```bash
# Clone the repo
git clone https://github.com/Abjith7/adk.git
cd adk

# Install dependencies
pip install -r requirements.txt

# Configure your API key
# Add GOOGLE_API_KEY to your .env file
GOOGLE_API_KEY=your_key_here
```

## Run any agent

```bash
# Example — run the tool agent
cd 2tool_agent
python agent.py
```

Each folder is self-contained — navigate into any agent directory and run directly.

## Learning path

This repo follows a deliberate progression:

```
Basic Agent → Tool Agent → LightLLM → Structured Outputs → Sessions
    ↓               ↓           ↓               ↓               ↓
Foundation     Add tools    Optimise       Production      Stateful
reasoning      & APIs       inference      outputs         memory
```

Start with `1basic_agent` if you're new to ADK. Each subsequent agent builds on the previous one.

## Why Google ADK?

ADK is Google's official framework for building production-grade AI agents. It provides native Gemini integration, built-in tool orchestration, and session management — making it the go-to choice for enterprise GenAI deployments on Google Cloud.

## Author

**Abjith A** — AI / GenAI Engineer  
[LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN) · [GitHub](https://github.com/Abjith7)
