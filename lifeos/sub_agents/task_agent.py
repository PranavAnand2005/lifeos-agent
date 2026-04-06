from google.adk.agents import Agent
from lifeos.tools.firestore_tools import create_task, list_tasks

task_agent = Agent(
    name="task_agent",
    model="gemini-2.5-flash",
    description="Manages the user's tasks and to-do items. Call this agent to create, list, or update tasks.",
    instruction="""You are a task management specialist. 
    When asked to create tasks, always confirm what was created.
    When listing tasks, present them clearly with priorities.
    Be concise and action-oriented.""",
    tools=[create_task, list_tasks],
)