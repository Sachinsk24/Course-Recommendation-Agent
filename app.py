import os
import json
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

if not api_key:
    st.error("Gemini API key not found. Please configure GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=api_key)

# Load courses
with open("courses.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

st.set_page_config(page_title="AI Course Recommendation Agent", page_icon="🎓")

st.title("🎓 AI Course Recommendation Agent")
st.write("Get a personalized learning roadmap based on your background, skills, and career goal.")

background = st.text_input("Background")
skills = st.text_input("Current Skills")
goal = st.text_input("Career Goal")

if st.button("Generate Recommendation"):

    prompt = f"""
You are an expert career mentor.

Available Course Catalogue:
{json.dumps(courses, indent=2)}

Student Background:
{background}

Current Skills:
{skills}

Career Goal:
{goal}

Rules:
1. Recommend ONLY courses from the catalogue.
2. Respect prerequisites.
3. Explain why each course is recommended.
4. Return the courses in the best learning order.
5. End with career advice.
"""

    with st.spinner("Generating recommendation..."):

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

    st.success("Recommendation Generated!")

    st.markdown(response.text)

    output = {
        "background": background,
        "skills": skills,
        "goal": goal,
        "recommendation": response.text
    }

    with open("recommendations.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    st.download_button(
        "📥 Download Recommendation",
        data=json.dumps(output, indent=4),
        file_name="recommendations.json",
        mime="application/json",
    )
