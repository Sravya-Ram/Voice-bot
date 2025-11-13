
# 🎤 Flask VoiceBot – Public Web Voice Assistant

A simple, user-friendly **voice-enabled chatbot** built with **Flask (Python)** and the **Web Speech API**.

This bot listens to your voice, understands predefined questions, and responds both **in text and speech** — without using any API keys or paid services.

---

## 🚀 Features

- 🎙️ **Voice Input** — browser SpeechRecognition API  
- 🔊 **Voice Output** — browser SpeechSynthesis TTS  
- 🧠 **Flask Backend** — handles intent matching  
- 🌐 **Deployable** — Render, PythonAnywhere, Railway  
- 🔐 **No API keys required**  
- 🖥️ **Beginner friendly**  

---

## 📁 Project Structure

```
voicebot_flask/
│
├── app.py
├── requirements.txt
├── Procfile
├── README.md
└── templates/
    └── index.html
```

---

## 🛠️ Installation (Run Locally)

### 1️⃣ Create and activate a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app
```bash
python app.py
```

### 4️⃣ Open the app in your browser  
👉 http://127.0.0.1:5000

Allow microphone access and start using the voice bot.

---

## 🌍 Deployment Guide

### ▶ Deploy on Render (Recommended)
1. Push project to GitHub  
2. Create **New Web Service** in Render  
3. Build command:
```
pip install -r requirements.txt
```
4. Start command:
```
gunicorn app:app
```

### ▶ Deploy on PythonAnywhere
- Upload project files  
- Configure WSGI  
- Set virtual environment  
- Reload web app  

### ▶ Deploy on Railway / Hypercorn
Use same Gunicorn start command.

---

## 💬 Supported Questions

Examples:

- “Tell me your life story”  
- “What’s your superpower?”  
- “Top 3 areas you want to grow in?”  
- “What misconceptions do coworkers have about you?”  
- “How do you push your boundaries?”  

---

## 🧩 Customization

Edit:

- `app.py` → logic, intents, responses  
- `templates/index.html` → UI, layout, JS voice code  

---

## 📝 License
MIT License — free to use, modify, and deploy.

---

## ❤️ Author  
Created by **Sravya**, guided by ChatGPT.
