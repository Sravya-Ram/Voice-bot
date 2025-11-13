import os, textwrap

# Create folders
os.makedirs("templates", exist_ok=True)

# Write app.py
with open("app.py", "w", encoding="utf-8") as f:
    f.write(textwrap.dedent("""
    from flask import Flask, render_template, request, jsonify
    import re, random

    app = Flask(__name__)

    def random_choice(arr): return random.choice(arr)

    def life_story():
        variants = [
            "I am  Ballepalli Lakshmi sravya,a computer science graduate from RGUKT,IIIT Ongole .My academic journey included extensive hands on experience with programming languages such as python,c,c++ and database querying using sql as well as technologies like huggingface,langchain,flask.I did  a project named atliq tees which converts the english text into sql query and reply back in english text which is very
            helpful for business people to know about stock maintainance so and so with the help of python, langchain and hugging face embeddings.I worked as  computer science tutor in cheggfor 3 months. .",
            "Now I am currently  a housewife ,being housewife I learnt endurance,to being motivated everyday and dedication towards my work.",
            "A few sentences: curious learner, practical problem-solver, loves reading books(fav book: atomic habits). I try to be concise and friendly while being useful."
        ]
        return random_choice(variants) + " Would you like a shorter version?"

    def superpower():
        variants = [
            "My superpower is adaptability and continuous learning, staying ahead of fast-evolving advances in ai technology",
            "Understanding the complex problems and breaking then into smaller ones in order to find  solution.",
            "Turning ambiguity into a clear plan — that’s my strength."
        ]
        return random_choice(variants)

    def grow_areas(mode='concise'):
        modes = {
            "concise": "technical depth, leadership, and public speaking.",
            "friendly": "deeper engineering knowledge, leading bigger projects, and speaking with confidence.",
            "professional": "domain mastery, and leadership."
        }
        return "Top three areas I'd like to grow in: " + modes.get(mode, modes["concise"])

    def misconception():
        return "People think I'm always formal and strict — but I can be friendly too!"

    def push_boundaries():
        return "I challenge myself through continuous learning. I set quarterly goals, take micro-courses, and practice new skills on small internal tasks before applying them to bigger projects.
        This approach helps me grow steadily and stay adaptable.."

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
    """))

# Write templates/index.html
with open("templates/index.html", "w", encoding="utf-8") as f:
    f.write(textwrap.dedent("""
    <!doctype html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>Flask VoiceBot</title>
    </head>
    <body style="font-family:Arial">
    <h1>Flask VoiceBot</h1>
    <button onclick="startListening()">🎤 Start Listening</button>
    <button onclick="stopListening()">Stop</button><br><br>

    <textarea id="typed" placeholder="Type a question..." style="width:300px;height:80px"></textarea>
    <button onclick="sendTyped()">Send</button>

    <div id="chat" style="margin-top:20px"></div>

    <script>
    let rec=null;

    if('webkitSpeechRecognition' in window){
        rec=new webkitSpeechRecognition();
        rec.lang='en-US';
        rec.onresult=e=>{
            let text=e.results[0][0].transcript;
            send(text);
        };
    }

    function startListening(){ if(rec) rec.start(); }
    function stopListening(){ if(rec) rec.stop(); }

    function sendTyped(){
        let t=document.getElementById('typed').value;
        send(t);
    }

    function send(text){
        add('You: '+text);
        fetch('/api/respond',{
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({text:text})
        }).then(r=>r.json()).then(j=>{
            add('Bot: '+j.reply);
            speak(j.reply);
        });
    }

    function add(t){
        let div=document.getElementById('chat');
        div.innerHTML += "<p>"+t+"</p>";
    }

    function speak(t){
        let u=new SpeechSynthesisUtterance(t);
        speechSynthesis.speak(u);
    }
    </script>
    </body>
    </html>
    """))

# Write requirements
with open("requirements.txt", "w") as f:
    f.write("Flask\n")

print("Project created successfully!")


