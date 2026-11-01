import os
import anthropic
from dotenv import load_dotenv, find_dotenv

# 1. Load environment variables
load_dotenv(find_dotenv())

# Check for standard ANTHROPIC_API_KEY first, fallback to API_KEY
api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("API_KEY")

if not api_key:
    raise ValueError(
        "API Key not found! Please check that your .env file defines ANTHROPIC_API_KEY or API_KEY."
    )

# 2. Initialize Anthropic client (Anthropic class, not module call)
client = anthropic.Anthropic(api_key=api_key)

# 3. Define Tools
# The tools array tells Claude what tools are available:
# name, description, and JSON schema defining the required input arguments.
tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a city.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get weather for",
                }
            },
            "required": ["city"],
        },
    }
]


# 4. Tool Execution Handler
# In production, this would query an external API, database, or service.
def run_tool(name, tool_input):
    if name == "get_weather":
        city = tool_input.get("city", "Unknown")
        return f"Weather in {city}: 95°F, sunny"
    raise ValueError(f"Unknown tool: {name}")


# 5. Initialize conversation
messages = [
    {"role": "user", "content": "What should I wear in Austin today?"}
]

# 6. The Agent Loop (ReAct / Tool-Use Loop)
# Iterates until Claude finishes with 'end_turn' or max iterations reached.
max_iterations = 5
current_iteration = 0

canPass =True

while current_iteration < max_iterations or canPass:
    current_iteration += 1

    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

    # Optional: Print intermediate text/thoughts if Claude produced any
    for block in response.content:
        if block.type == "text" and response.stop_reason == "tool_use":
            print(f"[Claude Thought]: {block.text}")

    # Case A: Claude completed its final answer
    if response.stop_reason == "end_turn":
        print("\n[Final Answer]:")
        for block in response.content:
            if block.type == "text":
                print(block.text)
        break

    # Case B: Claude requested one or more tool calls
    elif response.stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"[Tool Call]: {block.name}(input={block.input})")
                result = run_tool(block.name, block.input)
                print(f"[Tool Result]: {result}")
                tool_results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    }
                )

        # Feed back both the assistant's turn and the user's tool results
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
        canPass =False

    else:
        # Handle unexpected stop reasons (e.g. max_tokens)
        print(f"Warning: Loop stopped with reason: {response.stop_reason}")
        break