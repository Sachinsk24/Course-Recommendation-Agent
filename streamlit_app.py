import os
import json
import time
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Load courses
with open("courses.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

# Page configuration
st.set_page_config(
    page_title="AI Course Recommendation Agent",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Course Recommendation Agent")
st.write("Get a personalized learning roadmap based on your background and career goal.")

# User inputs
background = st.text_input("🎓 Background", placeholder="Example: B.Tech CSE")
skills = st.text_input("💻 Current Skills", placeholder="Example: Python, SQL")
goal = st.text_input("🎯 Career Goal", placeholder="Example: Data Scientist")

if st.button("🚀 Recommend Courses"):

    if not background or not skills or not goal:
        st.warning("Please fill in all fields.")
    else:
        prompt = f"""
You are an expert career mentor.

Available Course Catalogue:
{json.dumps(courses, indent=2)}

Student Profile:
Background: {background}
Skills: {skills}
Career Goal: {goal}

Rules:
1. Recommend ONLY courses from the catalogue.
2. Respect prerequisites.
3. Explain why each course is recommended.
4. Return the learning path in the correct order.
5. End with career advice.
"""

        with st.spinner("Generating recommendation..."):

            response = None

            for attempt in range(3):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt
                    )
                    break

                except Exception as e:
                    if attempt < 2:
                        time.sleep(5)
                    else:
                        st.error(f"Error: {e}")
                        st.stop()

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
            label="📥 Download Recommendation (JSON)",
            data=json.dumps(output, indent=4, ensure_ascii=False),
            file_name="recommendations.json",
            mime="application/json"
        )