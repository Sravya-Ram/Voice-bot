
from flask import Flask, render_template, request, jsonify
import re, random

app = Flask(__name__)

def random_choice(arr): return random.choice(arr)

def life_story():
    variants = [
        "I  am Ballepalli Lakshmi Sravya,Computer science graduate from Rgukt IIIT Ongole.“I’ve always been fascinated by how technology can understand people. I started with a strong foundation in software engineering, and gradually shifted into Generative AI by working on projects that involved LLMs, automation, and conversational systems. Over time, I developed skills in building AI agents, prompt engineering, and deploying real-world Gen AI applications. Today, I enjoy creating AI tools that make tasks easier, faster, and more human-like recently I have developed a project atliq tees which converts english text into sql query and reply back in english text which is developed by using python,langchain,huggingface embeddings and sql query", 
        "In short: I've always been curious — I read a lot, love to work and always try to gain knowledge and improve myself consistently",
        "A few sentences: curious learner, practical problem-solver, loves reading. I try to be concise and friendly while being useful."
    ]
    return random_choice(variants) + " Would you like a shorter version?"

def superpower():
    variants = [
        "My super power is my understanding ability which helps me to break complex problems into little ones and find solution.",
        "Active listening is definitely my superpower.",
        "Turning ambiguity into a clear plan — that’s my strength."
    ]
    return random_choice(variants)

def grow_areas(mode='concise'):
    modes = {
        "concise": "technical depth, leadership, and public speaking.",
        "friendly": "deeper engineering knowledge, leading bigger projects, and speaking with confidence.",
        "professional": "domain mastery, leadership."
    }
    return "Top three areas I'd like to grow in: " + modes.get(mode, modes["concise"])

def misconception():
    return "People think I'm always formal and strict — but I can be friendly too!"

def push_boundaries():
    return "“I push my limits by staying calm under pressure and using tight deadlines as an opportunity to test my efficiency. I prioritize sharply, simplify tasks, and communicate proactively. This helps me deliver quality work even in challenging situations"

def fallback():
    return "That's interesting! Could you rephrase or ask in another way?"

PATTERNS = [
    (re.compile(r"life story|about your life", re.I), life_story),
    (re.compile(r"superpower|super power", re.I), superpower),
    (re.compile(r"top 3|three areas|grow in", re.I), grow_areas),
    (re.compile(r"misconception|coworkers", re.I), misconception),
    (re.compile(r"push boundaries|push your limits", re.I), push_boundaries),
    (re.compile(r"hello|hi|hey", re.I), lambda: "Hi! How can I help?"),
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/respond", methods=["POST"])
def respond():
    data = request.json
    text = data.get("text", "")
    mode = data.get("mode", "concise")

    for pattern, func in PATTERNS:
        if pattern.search(text):
            if func in (grow_areas,):
                return jsonify({"reply": func(mode)})
            return jsonify({"reply": func()})

    return jsonify({"reply": fallback()})

if __name__ == "__main__":
    app.run(debug=True)
