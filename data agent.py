from agents import Agent

data_agent = Agent(
    name="Data Analyst Agent",
    instructions="""
    You are a professional data analyst.
    Your tasks:
    1. Understand the user's data-analysis request.
    2. Generate Python code.
    3. Analyze the results.
    4. Explain the findings clearly.
    """
)
