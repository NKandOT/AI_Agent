import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None: raise RuntimeError("No API key found")
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="user prompt")
args = parser.parse_args()
user_prompt = args.user_prompt
client = OpenAI(
	base_url="https://openrouter.ai/api/v1",
	api_key=api_key,
)
agent_output = client.chat.completions.create(
	model="openrouter/free",
	messages=[
		{
			"role": "user",
			"content": user_prompt,
		}
	]
)
if agent_output.usage is None: raise RuntimeError("No usage data returned from API.")
prompt_tokens = agent_output.usage.prompt_tokens
response_tokens = agent_output.usage.completion_tokens
print(f"User prompt: {user_prompt}")
print(f"Prompt tokens: {prompt_tokens}")
print(f"Response tokens: {response_tokens}")
print("Response: ")
print(agent_output.choices[0].message.content)
