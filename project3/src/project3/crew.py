# from crewai import Agent, Crew, Process, Task, LLM
# from crewai.project import CrewBase, agent, crew, task
# from dotenv import load_dotenv
# from crewai_tools import SerperDevTool
# load_dotenv()
# # Uncomment the following line to use an example of a custom tool
# # from project3.tools.custom_tool import MyCustomTool

# # Check our tools documentations for more information on how to use them
# # from crewai_tools import SerperDevTool

# @CrewBase
# class Project3():
# 	"""Project3 crew"""

# 	agents_config = 'config/agents.yaml'
# 	tasks_config = 'config/tasks.yaml'

# 	llm = LLM(
# 		model="groq/llama-3.1-8b-instant",
# 		temperature=0.7
# 	)

# 	@agent
# 	def JobScout(self) ->Agent:
# 		return Agent(
# 			config=self.agents_config['JobScout'],
# 			tools=[SerperDevTool()],
# 			verbose=True,
# 			llm=self.llm
# 		)

# 	@agent
# 	def interview_ace(self) -> Agent:
# 		return Agent(
# 			config=self.agents_config['interview_ace'],
# 			tools=[SerperDevTool()],
# 			verbose=True,
# 			llm=self.llm
# 		)

# 	@task
# 	def job_search_task(self) -> Task:
# 		return Task(
# 			config=self.tasks_config['job_search_task'],
# 		)
	
# 	@task
# 	def interview_task(self) -> Task:
# 		return Task(
# 			config=self.tasks_config['interview_task'],
# 		)
	
# 	@task
# 	def guide_task(self) -> Task:
# 		return Task(
# 			config=self.tasks_config['guide_task'],
# 		)

# 	@crew
# 	def crew(self) -> Crew:
# 		"""Creates the Project3 crew"""
# 		return Crew(
# 			agents=self.agents, # Automatically created by the @agent decorator
# 			tasks=self.tasks, # Automatically created by the @task decorator
# 			process=Process.sequential,
# 			verbose=True,
# 			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
# 		)
from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

class CompanyInfo(BaseModel):
    """Company information model"""
    culture: str = Field(..., description="Company culture")
    rating: float = Field(..., description="Company rating")
    office_timings: str = Field(..., description="Office timings")
    salary: str = Field(..., description="Salary details")
    responsibilities: List[str] = Field(..., description="Job responsibilities")

class InterviewDetails(BaseModel):
    """Interview process details model"""
    stages: List[str] = Field(..., description="Interview stages")
    questions: List[str] = Field(..., description="Expected interview questions")

@CrewBase
class JobAssistanceCrew():
    """Job Assistance crew for helping with job search and interview preparation"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    llm = LLM(
        model="groq/llama-3.1-8b-instant",
        temperature=0.7
    )

    @agent
    def job_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['job_scout'],
            tools=[SerperDevTool()],
            verbose=True,
            llm=self.llm
        )

    @agent
    def interview_ace(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_ace'],
            tools=[SerperDevTool()],
            verbose=True,
            llm=self.llm
        )

    @task
    def research_job_company(self) -> Task:
        return Task(
            config=self.tasks_config['research_job_company'],
            agent=self.job_scout(),
            output_json=CompanyInfo
        )

    @task
    def research_interview_process(self) -> Task:
        return Task(
            config=self.tasks_config['research_interview_process'],
            agent=self.job_scout(),
            output_json=InterviewDetails
        )

    @task
    def prepare_interview_guidance(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_interview_guidance'],
            agent=self.interview_ace(),
            context=[self.research_interview_process()],
            output_file='interview_preparation.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Job Assistance crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
