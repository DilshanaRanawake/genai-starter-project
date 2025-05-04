# 🧠 GenAI Starter Project

A simple FastAPI application that generates text using Hugging Face Transformers (GPT-2).  
Perfect for getting started with generative AI, REST APIs, and backend integration.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green.svg)](https://fastapi.tiangolo.com/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-transformers-yellow.svg)](https://huggingface.co/docs/transformers)

---

## 📚 Table of Contents

- [🚀 Features](#-features)
- [🛠️ Setup Instructions](#️-setup-instructions)
- [▶️ Run the App](#️-run-the-app)
- [🧪 Example Output](#-example-output)
- [📁 Project Structure](#-project-structure)
- [📚 What I Learned](#-what-i-learned)
- [🖼️ Screenshots](#️-screenshots)
- [📌 Next Steps](#-next-steps)
- [📄 License](#-license)

---

## 🚀 Features

- 🧾 Text generation using Hugging Face Transformers (`gpt2`)
- ⚡ FastAPI backend for ML model serving
- 🧪 Swagger UI for interactive API testing
- 📁 Clean project structure
- 📦 Easy to expand or integrate with agentic AI tools

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/genai-starter-project.git
cd genai-starter-project
```
### 2. Create and activate a virtual environment

```bash
python -m venv genai-env
source genai-env/bin/activate       # Windows: .\genai-env\Scripts\activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
---

## ▶️ Run the App
```bash
uvicorn app:app --reload
```
Open your browser and go to: http://127.0.0.1:8000/docs

Use the /generate endpoint with input like:

```bash
{
  "text": "Once upon a time"
}
```
---

## 🧪 Example Output
propmt:
```bash
AI will change the world by
```
output:
```bash
AI will change the world by helping machines understand and support human decision-making in ways never before possible.
```

---

## 📁 Project Structure

```bash
genai-starter-project/
├── app.py               # FastAPI application
├── requirements.txt     # Python dependencies
├── .gitignore
├── README.md
├── .env.example         # Placeholder for future API keys
├── models/              # (Optional) Custom models or configs
├── pics/                # Screenshots and visual assets
```

---

## 📚 What I Learned
✅ Python & FastAPI
- Refreshed core Python: functions, classes, and file handling.
- Built a REST API using FastAPI with Pydantic models.

✅ Hugging Face Transformers
- Loaded gpt2 using pipeline("text-generation").
- Sent prompts and received generated completions.

✅ Model Serving via API
- Exposed ML model using a FastAPI POST endpoint.
- Parsed JSON input and returned generated text as a response.

✅ Swagger UI & API Testing
- Used FastAPI’s built-in Swagger docs (/docs) to:
- Test endpoints interactively
- Debug response structure and status

✅ Clean Code Practices
- Set up .gitignore to avoid unnecessary files.
- Created .env.example to prepare for secure API key use.

---

## 🖼️ Screenshots
![](https://github.com/DilshanaRanawake/genai-starter-project/blob/main/pics/Screenshot%202025-05-03%20135610.png)
![](https://github.com/DilshanaRanawake/genai-starter-project/blob/main/pics/Screenshot%202025-05-03%20135732.png)
![](https://github.com/DilshanaRanawake/genai-starter-project/blob/main/pics/Screenshot%202025-05-03%20135756.png)


