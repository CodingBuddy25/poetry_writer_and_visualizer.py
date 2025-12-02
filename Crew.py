from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import FileReadTool
from crewai_tools import FileWriterTool

@CrewBase
class PoetryCrew():
    """Poetry crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    @agent
    def story_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['story_agent'],
            tools=[FileReadTool(),FileWriterTool()],
            verbose=True
        )


    @agent
    def poet_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['poet_agent'],
            tools=[FileReadTool()],
            verbose=True,
        )

    @agent
    def poetry_editor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['poetry_editor_agent'],
            tools=[FileReadTool(),FileWriterTool()],
            verbose=True,
        )

    @agent
    def designing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['designing_agent'],
            verbose=True,
        )



    @agent
    def critique_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['critique_agent'],
            tools=[FileReadTool(),FileWriterTool()],
            verbose=True,
        )

    @task
    def story_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['story_agent_task'],
        )

    @task
    def poet_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['poet_agent_task'],
        )

    @task
    def poetry_editor_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['poetry_editor_agent_task'],
        )

    @task
    def designing_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['designing_agent_task'],
        )

    @task
    def critique_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['critique_agent_task'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Dinsdag crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
