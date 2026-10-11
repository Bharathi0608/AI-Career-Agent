import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("GROQ_API_KEY is missing from environment variables")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=api_key
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


# def suggest_jobs_ai(skills):

#     prompt = f"""
#     Based on these skills:

#     {skills}

#     Suggest:

#     1. Best job roles
#     2. Career path
#     3. Salary range

#     Return clearly.
#     """

#     response = llm.invoke(prompt)

#     return response.content


def suggest_jobs_ai(skills, resume_text=""):

    prompt = f"""
You are an AI career advisor. Analyze this specific candidate's resume.

EXTRACTED SKILLS:
{skills}

FULL RESUME:
{resume_text}

Create personalized career recommendations using evidence from this resume.

Include:
1. Best 5 job roles, ranked by suitability.
2. For each role, explain which skills, projects, or experience make
   the candidate suitable and identify any skill gaps.
3. A realistic entry-level career roadmap with stages and milestones.
4. Approximate annual salary ranges for India in INR.
5. Three concrete actions the candidate should take next.

Rules:
- Base recommendations on the supplied resume, not an imagined candidate.
- Mention actual projects, technologies, education, and experience
  only when present in the resume.
- Do not invent employment history, achievements, or qualifications.
- If information is missing, explicitly say it is not provided.
- Treat this candidate's resume independently of previous candidates.
- Use clear headings and numbered lists.
- Do not use Markdown tables or pipe separators.
- Keep the recommendations relevant to the candidate's experience level.
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


# def interview_questions_ai(skills):

#     prompt = f"""
#     Generate 15 interview questions with detailed answers for these skills:

#     {skills}

#     Format each question and answer as:
#     Question: [question text]
#     Answer: [detailed answer]

#     Make the answers comprehensive and helpful for interview preparation.
#     """

#     response = llm.invoke(prompt)

#     return response.content


def interview_questions_ai(skills):

    prompt = f"""
You are an experienced technical interviewer and interview coach.

Generate exactly 15 technical interview questions with detailed,
accurate answers based on these skills:

{skills}

STRICT OUTPUT FORMAT:
Use the following format for EVERY question:

1. [Write one clear interview question]
Answer: [Provide a specific, technically accurate answer in 3-6 sentences.]

2. [Write the next interview question]
Answer: [Provide a specific answer in 3-6 sentences.]

Continue numbering consecutively through 15.

IMPORTANT RULES:
- Every question MUST have its own answer.
- Put each question on a new line.
- Start each answer with exactly "Answer:" on a new line.
- Never omit an answer or repeat a generic answer.
- Explain technical concepts clearly and include examples where useful.
- Focus on the supplied skills; do not introduce unrelated technologies.
- Avoid Markdown tables, pipe separators, and code fences.
- Do not include an introduction or conclusion outside the 15 Q&A pairs.
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
