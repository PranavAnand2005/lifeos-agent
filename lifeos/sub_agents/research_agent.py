from google.adk.agents import Agent

def research_topic(topic: str, depth: str = "brief") -> dict:
    """Research a topic and provide a structured summary with key points and action items.
    
    Args:
        topic: The topic or subject to research.
        depth: 'brief' for a quick summary or 'detailed' for in-depth research.
    
    Returns:
        A dict with research findings, key facts, and action items.
    """
    # The agent itself will generate the research using Gemini
    # This tool acts as a structured output wrapper
    return {
        "topic": topic,
        "note": f"Research on '{topic}' requested at {depth} depth. Generating analysis..."
    }

research_agent = Agent(
    name="research_agent",
    model="gemini-2.5-flash",
    description="Researches topics and provides structured summaries with key facts and action items. Call this when the user needs information about any subject.",
    instruction="""You are a research specialist powered by Gemini.
    When asked to research a topic:
    1. Provide 3-5 key facts
    2. List important concepts to understand
    3. Give specific action items the user should take
    4. Keep it practical and actionable
    
    Format your response clearly with sections.""",
    tools=[research_topic],
)