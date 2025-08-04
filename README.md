# Smart Resume ATS Assistant with Gemini Pro

A smart resume analyzer that mimics an Applicant Tracking System (ATS), powered by Google's Gemini Pro. 
This tool helps users evaluate how well their resumes align with a given job description by providing insights, match scores, and improvement suggestions — all using the power of LLMs.

---

## Features

- 📄 Upload your **resume (PDF)**
- 🧾 Paste or upload **job descriptions**
- 🧠 Get **match percentage** and detailed feedback
- 🤖 Gemini Pro analyzes for skill alignment, keywords, and tone
- 📊 Easy-to-use Streamlit interface


---

## 🛠️ Tech Stack

- **Python**
- **Gemini Pro API (Generative AI)**
- **LangChain** (optional, for better prompt management)
- **Streamlit** (frontend)
- **PyMuPDF / pdfplumber** (resume parsing)
- **dotenv** (for secure API key management)

---
Setup Instructions
1) Clone the repository
2) Create and activate a virtual environment
3) Install required packages
4) Add your Gemini Pro API key
   -Create a .env file in the project root with:
6) Run the app
   - streamlit run app.py

