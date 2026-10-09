from agents import Agent

from tools import (
    inspect_csv,
    dataset_statistics
)


data_agent = Agent(
    name="Data Analyst Agent",

    instructions="""
You are a professional Data Analyst.

Your responsibilities:

1. Understand the user's dataset question.
2. Inspect CSV datasets.
3. Calculate statistics.
4. Identify useful patterns.
5. Explain results clearly.
6. Use the available tools when necessary.

Always provide a concise explanation of your findings.
""",

    tools=[
        inspect_csv,
        dataset_statistics
    ]
)


coding_agent = Agent(
    name="Python Coding Agent",

    instructions="""
You are a professional Python programmer.

Your responsibilities:

1. Understand programming requirements.
2. Write clean Python code.
3. Explain the code.
4. Find programming errors.
5. Suggest corrections.
6. Prefer readable and maintainable Python.
"""
)


manager_agent = Agent(
    name="Coding and Data Manager",

    instructions="""
You are the main manager of a Coding and Data AI system.

Decide which specialist should handle the user's request.

Use the Data Analyst Agent when:
- The task involves CSV files.
- The task involves pandas.
- The task involves data analysis.

Use the Python Coding Agent when:
- The user asks for Python code.
- The user asks to debug code.
- The user asks to design a Python program.

Return a clear final answer.
""",

    handoffs=[
        data_agent,
        coding_agent
    ]
)
