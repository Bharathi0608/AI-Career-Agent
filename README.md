# 🚀 AI Career Agent

An AI-powered Resume Analysis Platform built using **Python, Flask, LangGraph, LangChain, and Groq LLM**.

The system analyzes uploaded resumes and provides intelligent career guidance including skill extraction, job recommendations, resume scoring, interview preparation, and cover letter generation.

---

## 📌 Features

### 🔍 Resume Skill Extraction

* Extracts technical skills from uploaded resumes.
* Identifies programming languages, frameworks, databases, and tools.

### 💼 Job Recommendations

* Suggests suitable software development roles based on extracted skills.
* Provides career guidance for different technology stacks.

### 📊 Resume Scoring

* Evaluates resume quality and provides an overall score.
* Highlights strengths and areas for improvement.

### 🎯 Interview Question Generation

* Generates personalized interview questions based on detected skills.
* Helps candidates prepare for technical interviews.

### 📝 AI Cover Letter Generator

* Creates professional cover letters automatically from resume content.
* Saves time during job applications.

### 🤖 LangGraph Workflow

* Uses LangGraph StateGraph to orchestrate a multi-step AI workflow.
* Maintains state between different stages of analysis.

---

## 🏗️ System Architecture

Resume Upload

↓

PDF Parser (PyPDF2)

↓

LangGraph Agent Workflow

↓

Skill Extraction Agent

↓

Job Recommendation Agent

↓

Resume Scoring Agent

↓

Interview Question Agent

↓

Cover Letter Agent

↓

Results Dashboard

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### AI & Agent Frameworks

* LangChain
* LangGraph
* Groq LLM (Llama Models)

### Resume Processing

* PyPDF2

### Frontend

* HTML
* CSS

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
AI-Career-Agent/
│
├── app.py
├── agents.py
├── resume_agent.py
├── resume_parser.py
├── jobs.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── uploads/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Bharathi0608/AI-Career-Agent.git
cd AI-Career-Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

* ATS Resume Analysis
* Resume Keyword Optimization
* Learning Roadmap Generator
* Job Search API Integration
* LinkedIn Profile Analysis
* Resume PDF Report Export
* Multi-Agent Decision Routing

---

## 📸 Screenshots

Add screenshots of:

* Home Page
* Resume Upload
* AI Analysis Results
* Job Recommendations
* Resume Score Dashboard

---

## 👨‍💻 Author

**BHARATHI S**

Aspiring Software Developer | AI Enthusiast | Full Stack Developer

GitHub: https://github.com/Bharathi0608

---

## ⭐ Project Highlights

* AI-Powered Resume Analysis
* LangGraph Workflow Integration
* Groq LLM Integration
* Multi-Agent Architecture
* Career Guidance Automation
* Portfolio-Ready AI Project
