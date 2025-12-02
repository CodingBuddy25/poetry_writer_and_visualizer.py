# CrewAI for poetry writing and visualization

## Running the Script
To run the script, make sure that you run it in a python environment with a version between 3.10 and 3.14.

Make a .env file with your own OpenAI key. This will be used to create agents and enable interaction through AI usage.
The format is:
```OPENAI_API_KEY = sk-proj-...```. You can get it from this page https://platform.openai.com/api-keys. 

To run the code, run the python_writer_and_visualizer.py file. 

### Installing packages
Install CrewAI by using ```pip install crewai```.
Also make sure to install the other packages mentioned on top of the Crew.py
file. These are:

```
from crewai import Agent, Crew, Process, Task 
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import FileReadTool
from crewai_tools import FileWriterTool
```
The final package can be found in the Poetry_writer_and_visualizer.py file:
```from dotenv import load_dotenv```. This will be used to load the API key. 

## Documentation and references

Python package CrewAI: https://pypi.org/project/crewai/

Tutorial used to understand CrewAI: https://www.youtube.com/watch?v=q6QLGS306d0

CrewAI documentation: https://docs.crewai.com/en/introduction

Specific documentation used for the project:
1. https://docs.crewai.com/en/installation
2. https://docs.crewai.com/en/quickstart
3. https://docs.crewai.com/en/concepts/agents
4. https://docs.crewai.com/en/concepts/tasks#yaml-configuration-with-markdown
5. https://docs.crewai.com/en/concepts/knowledge
6. https://docs.crewai.com/en/concepts/tools#using-crewai-tools
