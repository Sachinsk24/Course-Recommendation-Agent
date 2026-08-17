import os
import json
import time
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Load course catalogue
with open("courses.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

print("=" * 50)
print("🎓 AI Course Recommendation Agent")
print("=" * 50)

# Get user input
background = input("Background: ")
skills = input("Current Skills: ")
goal = input("Career Goal: ")

# Create prompt
prompt = f"""
You are an expert career mentor.

Available Course Catalogue:
{json.dumps(courses, indent=2)}

Student Profile:
- Background: {background}
- Current Skills: {skills}
- Career Goal: {goal}

Instructions:
1. Recommend ONLY courses from the catalogue.
2. Follow all prerequisites.
3. Explain why each course is recommended.
4. Return the courses in the correct learning order.
5. End with career advice.
"""

# Call Gemini with retry logic
response = None

for attempt in range(3):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )
        break

    except Exception as e:
        print(f"\n❌ Attempt {attempt + 1} failed.")
        print(e)

        if attempt < 2:
            print("⏳ Retrying in 5 seconds...\n")
            time.sleep(5)
        else:
            print("\n🚫 Unable to connect to Gemini.")
            exit()

# Save recommendation
output = {
    "background": background,
    "skills": skills,
    "goal": goal,
    "recommendation": response.text
}

with open("recommendations.json", "w", encoding="utf-8") as file:
    json.dump(output, file, indent=4, ensure_ascii=False)

# Display recommendation
print("\n" + "=" * 50)
print("📚 Recommended Learning Path")
print("=" * 50)
print(response.text)

print("\n✅ Recommendation saved to recommendations.json")