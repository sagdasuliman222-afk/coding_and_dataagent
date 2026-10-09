import asyncio

from agents import Runner
from agents import set_default_openai_key

from dotenv import load_dotenv
import os

from agents import Agent

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OPENAI_API_KEY was not found.")
    print("Running Demo Mode instead.")

else:
    set_default_openai_key(api_key)


from agents import Agent

manager_agent = Agent(
    name="Coding and Data Manager",

    instructions="""
You are a Coding and Data Manager.

Handle Python programming and data analysis questions.

For data analysis:
- inspect datasets
- calculate statistics
- explain results

For programming:
- generate Python code
- debug code
- explain solutions
"""
)


async def main():

    print("=" * 60)
    print("CODING & DATA AGENT")
    print("=" * 60)

    question = input(
        "\nEnter your question:\n> "
    )

    result = await Runner.run(
        manager_agent,
        question
    )

    print("\n" + "=" * 60)
    print("AGENT RESULT")
    print("=" * 60)

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
