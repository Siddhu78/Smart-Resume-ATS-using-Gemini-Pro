import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini
def get_gemini_response(input):
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')
    response = model.generate_content(input)
    return response.text

# Function to extract text from uploaded PDF resume
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text() or "")
    return text

# Streamlit UI
st.title("Smart ATS Resume Evaluator")
st.markdown("Improve your resume with AI-powered ATS analysis.")

# Inputs from user
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume (PDF only)", type="pdf")

# Button
submit = st.button("Submit")

if submit:
    if uploaded_file is not None and jd.strip() != "":
        with st.spinner("Analyzing your resume..."):
            resume_text = input_pdf_text(uploaded_file)

            # Insert resume and JD into the prompt
            prompt = f"""
            Hey act like a skilled or very experienced ATS (Application Tracking System) with a deep understanding
            of tech field, software engineering, data science, data analytics and big data engineering. Your task is to 
            evaluate the resume based on the given job description.
            You must consider the job market is very competitive and you should provide the best assistance for improving the resume.
            Assign the percentage matching based on the JD and the missing keywords with high accuracy.

            resume: {resume_text}
            description: {jd}

            I want the response in one single string having the structure:
            {{"JD Match":"%", "MissingKeywords":[], "Profile Summary":""}}
            """

            # Get Gemini response
            raw_response = get_gemini_response(prompt)

            # Try parsing it as JSON
            try:
                cleaned_response = raw_response.strip().replace("```json", "").replace("```", "")
                result = json.loads(cleaned_response)

                st.subheader("✅ ATS Analysis Result")
                st.write(f"**🎯 JD Match:** {result.get('JD Match', 'N/A')}")
                st.write(f"**❌ Missing Keywords:** {', '.join(result.get('MissingKeywords', []))}")
                st.write(f"**📝 Profile Summary Suggestion:**\n{result.get('Profile Summary', '')}")

            except Exception as e:
                st.error("⚠️ Couldn't parse the response from Gemini. Here's the raw output:")
                st.code(raw_response)
    else:
        st.warning("Please upload a resume and paste a job description.")
