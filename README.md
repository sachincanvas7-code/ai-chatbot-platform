# Modular AI Chatbot Platform

> A build-it-yourself project. I'm building this incrementally to learn how a
> chatbot grows from a simple prompt-responder into a tool-using, memory-keeping,
> database-connected assistant.

**Stack:** Python · Streamlit · OpenAI API
**Source:** Curious PM — Week 4 (APIs for AI)

---

## What I'll learn
- How an LLM API call actually works (request, response, tokens, cost)
- Why LLMs are stateless — and how to give them memory with a history array
- Tool / function calling: letting the model call code (weather, search)
- Multi-tool orchestration and the reliability tradeoffs that come with it
- Connecting the bot to a database to answer questions over real data

## Build progression (each step = one commit)
- [ ] **Step 1 — Frontend:** a basic Streamlit chat UI (stays constant after this)
- [ ] **Step 2 — Basic chat:** send messages to OpenAI, render responses
- [ ] **Step 3 — Memory:** keep conversation history so the bot remembers
- [ ] **Step 4 — Tools:** add function calling (e.g. weather / web search)
- [ ] **Step 5 — Personality:** a system prompt that shapes the bot's voice
- [ ] **Step 6 — Database:** connect a DB and answer questions over it

## Setup
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add my own OpenAI key
streamlit run app.py
```

## Ship it (public link)
Deploy free on **Streamlit Community Cloud** → connect this GitHub repo → set
`OPENAI_API_KEY` in the app's Secrets. Public URL goes in the portfolio.

## Record it
60–120s: the problem → live demo → one thing I learned. Link goes in the portfolio.

---
*Starter scaffold. The implementation is mine, committed step by step.*
