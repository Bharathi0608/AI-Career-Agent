from agents import (
    extract_skills_ai,
    suggest_jobs_ai,
    score_resume_ai,
    interview_questions_ai,
    cover_letter_ai
)
from flask import Flask, render_template, request, jsonify
from resume_agent import resume_agent
# pyrefly: ignore [missing-import]
from PyPDF2 import PdfReader
from jobs import jobs
from dotenv import load_dotenv

import os
import webbrowser
import threading

load_dotenv()

app = Flask(__name__)

def clean_markdown(text):
    """Remove markdown formatting like ** from text"""
    if not text:
        return text
    return text.replace("**", "")

UPLOAD_FOLDER = "uploads"


def read_resume(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def extract_skills(resume_text):

    skill_database = [
        "Python",
        "Java",
        "JavaScript",
        "React",
        "Node.js",
        "Express",
        "MongoDB",
        "MySQL",
        "HTML",
        "CSS",
        "Bootstrap",
        "Firebase",
        "Flask",
        "Django",
        "Git",
        "GitHub",
        "AWS",
        "Docker",
        "Kubernetes",
        "Machine Learning",
        "AI",
        "LangChain",
        "LLM"
    ]

    found_skills = []

    for skill in skill_database:
        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    return "\n".join(found_skills)


def match_jobs(skills):

    results = []

    for job in jobs:

        score = 0

        for skill in job["skills"]:

            if skill.lower() in skills.lower():
                score += 1

        results.append({
            "title": job["title"],
            "score": score
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():

    resume = request.files["resume"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    resume.save(filepath)

    resume_text = read_resume(filepath)

    # Default values (IMPORTANT)
    skills = ""
    ai_jobs = ""
    resume_score = ""
    interview_questions = ""
    cover_letter = ""

    try:

        # AI Agent Features

        print("Running Resume Agent (Graph)...")

        result = resume_agent.invoke({
        "resume_text": resume_text
        })
    

        skills = clean_markdown(result["skills"])
        ai_jobs = clean_markdown(result["jobs"])
        resume_score = clean_markdown(result["score"])
        interview_questions = clean_markdown(result["questions"])
        cover_letter = clean_markdown(result["cover_letter"])       

        # print("Running extract_skills_ai...")
        # skills = extract_skills_ai(resume_text)

        # print("Running suggest_jobs_ai...")
        # ai_jobs = suggest_jobs_ai(skills)

        # print("Running score_resume_ai...")
        # resume_score = score_resume_ai(resume_text)

        # print("Running interview_questions_ai...")
        # interview_questions = interview_questions_ai(skills)

        # print("Running cover_letter_ai...")
        # cover_letter = cover_letter_ai(resume_text)


    except Exception as e:

        import traceback

        print("\n========== AI ERROR ==========")
        print(e)
        traceback.print_exc()   
        print("==============================\n")
        # Fallback System
        skills = extract_skills(resume_text)

        ai_jobs = "AI recommendation unavailable."

        resume_score = "Resume score unavailable."

        interview_questions = "Interview questions unavailable."

        cover_letter = "Cover letter unavailable."

    matched_jobs = match_jobs(skills)

    if request.headers.get("Accept") == "application/json" or request.is_json:
        return jsonify({
            "skills": skills,
            "jobs": matched_jobs,
            "ai_jobs": ai_jobs,
            "resume_score": resume_score,
            "interview_questions": interview_questions,
            "cover_letter": cover_letter
        })

    return render_template(
        "result.html",
        skills=skills,
        jobs=matched_jobs,
        ai_jobs=ai_jobs,
        resume_score=resume_score,
        interview_questions=interview_questions,
        cover_letter=cover_letter
    )
if __name__ == "__main__":
    def open_browser():
        webbrowser.open("http://127.0.0.1:5000")
    
    threading.Timer(1, open_browser).start()
    app.run(debug=False)