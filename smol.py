import os

from smolagents import CodeAgent, DuckDuckGoSearchTool, Tool, HfApiModel
from dotenv import load_dotenv, dotenv_values 
from tool import FindFilesTool

load_dotenv() 

HF_TOKEN = os.getenv("HF_TOKEN")

image_generation_tool = Tool.from_space(
    "black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generate an image from a prompt"
)

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct", token=HF_TOKEN)

find_files_tool = FindFilesTool()
agent = CodeAgent(tools=[image_generation_tool, find_files_tool], model=model)
# agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

# agent.run("Improve this prompt, then generate an image of it. prompt='A cat drawn in vector style'")

agent.run("Find all files with the extension '.webp'")
