from agents import Agent,Runner,OpenAIChatCompletionsModel,set_tracing_disabled
from dotenv import load_dotenv,find_dotenv
from openai import AsyncOpenAI
import os
import asyncio


load_dotenv(find_dotenv(),override=True)

api_key=os.getenv("GEMINI_API_KEY")
base_url=os.getenv("GEMINI_BASE_URL")
model_name=os.getenv("GEMINI_MODEL")

client=AsyncOpenAI(api_key=api_key,base_url=base_url)

model=OpenAIChatCompletionsModel(openai_client=client,model=str(model_name))

agent:Agent=Agent(name='Python Developer',instructions="You are a helpful agent which helps to write python code and teach python,if anyone ask other questions except python don't answer and just say I don't know",model=model)

prompt=input("Enter your question:")

result=Runner.run_sync(agent,prompt)

print(result.final_output)

