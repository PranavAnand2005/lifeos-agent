from google.adk.agents import Agent
from lifeos.tools.firestore_tools import save_note, get_notes

notes_agent = Agent(
    name="notes_agent",
    model="gemini-2.5-flash",
    description="Saves and retrieves notes, summaries, and information. Call this agent to store key information or retrieve past notes.",
    instruction="""You are a knowledge management specialist.
    When saving notes, create comprehensive but concise content.
    Always add relevant tags so notes can be found later.
    Structure notes clearly with key points.""",
    tools=[save_note, get_notes],
)