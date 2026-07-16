import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

def main():
	load_dotenv()
	api_key = os.environ.get("OPENROUTER_API_KEY")
	if api_key == None: raise RuntimeError("No API key found")
	parser = argparse.ArgumentParser(description="Chatbot")
	parser.add_argument("user_prompt", type=str, help="user prompt")
	parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
	args = parser.parse_args()
	user_prompt = args.user_prompt
	messages=[
		{
			"role": "user",
			"content": user_prompt,
		}
	]
	agent_output = create_agent(messages, api_key)
	if agent_output.usage is None: raise RuntimeError("No usage data returned from API.")
	prompt_tokens = agent_output.usage.prompt_tokens
	response_tokens = agent_output.usage.completion_tokens
	if args.verbose == True:
		print(f"User prompt: {user_prompt}")
		print(f"Prompt tokens: {prompt_tokens}")
		print(f"Response tokens: {response_tokens}")
		print("Response: ")
	print(agent_output.choices[0].message.content)

def create_agent(Messages, API_KEY):
	client = OpenAI(
		base_url="https://openrouter.ai/api/v1",
		api_key=API_KEY,
	)
	return client.chat.completions.create(
		model="openrouter/free",
		messages = Messages
	)

if __name__ == "__main__":
    main()