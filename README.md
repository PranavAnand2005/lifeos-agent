# LifeOS - Multi-Agent Productivity Assistant

A multi-agent AI system built with Google ADK and Gemini that helps users manage tasks, schedules, and information through natural language.

## What it does
One message triggers multiple specialist agents simultaneously:
- **Task Agent** - Creates and manages tasks in Firestore
- **Calendar Agent** - Schedules events and time blocks
- **Notes Agent** - Saves and retrieves notes
- **Research Agent** - Researches topics using Gemini

## Tech Stack
- Google ADK (Agent Development Kit)
- Gemini 1.5 Flash (Vertex AI)
- Cloud Firestore
- Google Cloud Run

## Live Demo
https://lifeos-agent-565939703230.us-central1.run.app

## Run Locally
```bash
git clone https://github.com/PranavAnand2005/lifeos-agent.git
cd lifeos-agent
pip install -r requirements.txt
adk web
```

## Architecture
User → Orchestrator Agent → [Task Agent, Calendar Agent, Notes Agent, Research Agent] → Firestore
