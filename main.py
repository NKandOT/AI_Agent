import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None: raise RuntimeError("No API key found")
client = OpenAI(
	base_url="https://openrouter.ai/api/v1",
	api_key=api_key,
)
agent_output = client.chat.completions.create(
	model="openrouter/free",
	messages=[
		{
			"role": "user",
			"content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
		}
	]
)
print(agent_output.choices[0].message.content)
