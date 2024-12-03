#Job Assistance AI Agents
This project aims to develop two AI agents, JobScout and InterviewAce, designed to help users secure job offers by providing comprehensive support throughout the job search and interview preparation process.

Agent Names and Roles
1. JobScout
Role: Job and Company Researcher

Tasks:

Job and Company Research:

Search for detailed information about the job role and company.

Explore websites like Glassdoor, AmbitionBox, Naukri, LinkedIn, Indeed, etc.

Gather data on:

Company culture

Ratings and reviews

Office timings

Salary information

Employee responsibilities

Interview Process Insight:

Research the interview process for the specified company.

Use platforms such as Glassdoor, AmbitionBox, Naukri, LinkedIn to gather information on interview stages and typical questions.

2. InterviewAce
Role: Interview Preparation Assistant

Tasks:

Interview Preparation:

Guide the user through preparation for each round of the interview process.

Compile previous interview questions and experiences from platforms like Glassdoor, Naukri, LinkedIn, AmbitionBox, InterviewBit, Indeed, and other relevant sources.

Detailed Guidance:

Provide information and tips for each interview stage.

Create a set of expected interview questions for each round based on gathered data.

Offer personalized advice and strategies for preparation based on the job role and company-specific information.

Workflow
Input:

User provides the job role and company name.

JobScout:

Conducts thorough research on the job role and company.

Compiles and presents information on company culture, ratings, office timings, salary, job responsibilities, and interview process.

Output from JobScout:

Job offer details (job description, responsibilities, salary, etc.).

Company information (culture, rating, office timing, etc.).

Interview process details (rounds, expected questions, etc.).

Selection:

User selects a job offer and decides to prepare for the interview.

InterviewAce:

Guides the user through interview preparation for each stage.

Searches for previous interview questions and experiences.

Generates a context about the company and job role.

Prepares a set of expected interview questions for each round.

Output from InterviewAce:

Expected interview questions for each round.

Guidance on how to answer common interview questions.

Practice interview questions and answers.

Preparation:

User practices and prepares for each round of the interview with the help of InterviewAce.

Result:

User feels confident and prepared for the interview.

Benefits
Comprehensive Support: From job search to interview preparation, users receive end-to-end assistance.

Thorough Research: Detailed insights into company culture, job responsibilities, and interview processes.

Effective Preparation: Personalized guidance and practice questions to help users ace their interviews.

Running the Project
Prerequisites
Python 3.8 or higher

Required Python packages listed in requirements.txt

Installation
Clone the repository:

git clone https://github.com/ravivarmanr26/crewai.git
cd crewai/project3
Install the required packages:

pip install -r requirements.txt
Set up environment variables:

Create a .env file and add any necessary environment variables.

Usage
To run the Job Assistance AI Agents, you can use the following command:

bash
python main.py
To train the agents with specified iterations, use:

bash
python main.py train <number_of_iterations>
License
This project is licensed under the MIT License.

This README file provides a comprehensive overview of the project, including the roles and tasks of each agent, the workflow, benefits, installation instructions, and usage. Feel free to modify it based on any additional requirements or information specific to your project.

