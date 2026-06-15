import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def extract_skills_ai(resume_text):

    prompt = f"""
    Analyze this resume.

    Extract:
    - Technical Skills
    - Frameworks
    - Databases
    - Tools

    Resume:

    {resume_text}

    Return in bullet points.
    """

    response = llm.invoke(prompt)

    return response.content


def suggest_jobs_ai(skills):

    prompt = f"""
    Based on these skills:

    {skills}

    Suggest:

    1. Best job roles
    2. Career path
    3. Salary range

    Return clearly.
    """

    response = llm.invoke(prompt)

    return response.content
# ADD BELOW THIS LINE

def score_resume_ai(resume_text):

    prompt = f"""
    Analyze this resume.

    Give:
    1. Resume score out of 100
    2. Strengths
    3. Weaknesses
    4. Suggestions

    Resume:

    {resume_text}
    """

    response = llm.invoke(prompt)

    return response.content


def interview_questions_ai(skills):

    prompt = f"""
    Generate 15 interview questions with detailed answers for these skills:

    {skills}

    Format each question and answer as:
    Question: [question text]
    Answer: [detailed answer]

    Make the answers comprehensive and helpful for interview preparation.
    """

    response = llm.invoke(prompt)

    return response.content


def cover_letter_ai(resume_text):

    prompt = f"""
    Create a professional cover letter
    based on this resume:

    {resume_text}
    """

    response = llm.invoke(prompt)

    return response.content