from google.adk.agents import Agent
from lifeos.tools.firestore_tools import schedule_event

calendar_agent = Agent(
    name="calendar_agent",
    model="gemini-2.5-flash",
    description="Manages calendar events and schedules time blocks. Call this agent to schedule meetings, study sessions, or any time-based event.",
    instruction="""You are a calendar and scheduling specialist.
    Always confirm the exact time and duration when scheduling events.
    If a date is vague like 'tomorrow', keep it as-is and store it clearly.
    Be precise about scheduling details.""",
    tools=[schedule_event],
)