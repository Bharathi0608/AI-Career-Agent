from typing import TypedDict
# pyrefly: ignore [missing-import]
from langgraph.graph import StateGraph, END

from agents import (
    extract_skills_ai,
    suggest_jobs_ai,
    score_resume_ai,
    interview_questions_ai,
    cover_letter_ai
)

class ResumeState(TypedDict):
    resume_text: str
    skills: str
    jobs: str
    score: str
    questions: str
    cover_letter: str


def extract_node(state):
    state["skills"] = extract_skills_ai(state["resume_text"])
    return state


def jobs_node(state):
    state["jobs"] = suggest_jobs_ai(state["skills"])
    return state


def score_node(state):
    state["score"] = score_resume_ai(state["resume_text"])
    return state


def questions_node(state):
    state["questions"] = interview_questions_ai(state["skills"])
    return state


def cover_node(state):
    state["cover_letter"] = cover_letter_ai(
        state["resume_text"]
    )
    return state


graph = StateGraph(ResumeState)

graph.add_node("extract", extract_node)
graph.add_node("jobs", jobs_node)
graph.add_node("score", score_node)
graph.add_node("questions", questions_node)
graph.add_node("cover", cover_node)

graph.set_entry_point("extract")

graph.add_edge("extract", "jobs")
graph.add_edge("jobs", "score")
graph.add_edge("score", "questions")
graph.add_edge("questions", "cover")
graph.add_edge("cover", END)

resume_agent = graph.compile()