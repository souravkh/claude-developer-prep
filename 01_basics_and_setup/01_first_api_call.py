import os
import anthropic
from dotenv import load_dotenv, find_dotenv

# Automatically locate and load the .env file from root or parent directories
load_dotenv(find_dotenv())

# Check for standard ANTHROPIC_API_KEY first, fallback to API_KEY
api_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("API_KEY")

if not api_key:
    raise ValueError(
        "API Key not found! Please check that your .env file defines ANTHROPIC_API_KEY or API_KEY."
    )

# Initialize the Anthropic client
client = anthropic.Anthropic(api_key=api_key)

# Make the API call
# Using claude-haiku-5-5 for fast and cost-effective testing
message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, world!"}
    ],
)

# Extract and display the response
for block in message.content:
    if block.type == "text":
        print(block.text)

print(f"\nStop Reason: {message.stop_reason}")
print(f"Tokens Used -> Input: {message.usage.input_tokens}, Output: {message.usage.output_tokens}")
