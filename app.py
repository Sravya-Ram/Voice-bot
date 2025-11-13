
from flask import Flask, render_template, request, jsonify
import re, random

app = Flask(__name__)

def random_choice(arr): return random.choice(arr)

def life_story():
    variants = [
        "I grew up loving stories and building small projects. I trained on a wide range of texts and conversations, and now I enjoy helping people clarify ideas and practice interviews.",
        "In short: I've always been curious — I read a lot, practiced communicating clearly, and now I help people by answering questions and role-playing conversations.",
        "A few sentences: curious learner, practical problem-solver, loves a good explanation. I try to be concise and friendly while being useful."
    ]
    return random_choice(variants) + " Would you like a shorter version?"

def superpower():
    variants = [
        "My number one superpower is breaking complex ideas into simple steps.",
        "Active listening is definitely my superpower.",
        "Turning ambiguity into a clear plan — that’s my strength."
    ]
    return random_choice(variants)

def grow_areas(mode='concise'):
    modes = {
        "concise": "technical depth, leadership, and public speaking.",
        "friendly": "deeper engineering knowledge, leading bigger projects, and speaking with confidence.",
        "professional": "domain mastery, stakeholder communication, and leadership."
    }
    return "Top three areas I'd like to grow in: " + modes.get(mode, modes["concise"])

def misconception():
    return "People think I'm always formal — but I can be friendly too!"

def push_boundaries():
    return "I push boundaries by taking on tasks slightly outside my comfort zone."

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
