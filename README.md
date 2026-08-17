# 🎓 AI Course Recommendation Agent

An AI-powered course recommendation system built using Python, Google Gemini AI, and Streamlit.

## Features

- Personalized learning roadmap
- Uses a custom course catalogue
- Respects course prerequisites
- Interactive Streamlit web interface
- Saves recommendations as JSON
- Includes sample student profiles

## Tech Stack

- Python
- Google Gemini API
- Streamlit
- JSON
- python-dotenv

## Project Structure

```
course-recommendation-agent/
│── app.py
│── streamlit_app.py
│── courses.json
│── students.json
│── recommendations.json
│── requirements.txt
│── README.md
│── .gitignore
│── .env
```

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

Run the terminal version:

```bash
python app.py
```

Run the web app:

```bash
python -m streamlit run streamlit_app.py
```

## Sample Goals

- Web Developer
- Data Scientist
- Android Developer
- Backend Developer

## Sample Inputs/outputs
🎓 AI Course Recommendation Agent
Get a personalized learning roadmap based on your background and career goal.

🎓 Background-- B.Tech CSE
💻 Current Skills--Python, SQL
🎯 Career Goal--Web Developer

## Output
Hello! As your career mentor, I'm thrilled to help you build a clear, structured roadmap to achieve your goal of becoming a Web Developer.

Given your B.Tech CSE background and existing knowledge of Python and SQL, you already have a solid foundation. We will leverage your existing skill set to accelerate your learning while building essential modern frontend, backend, and deployment skills.

Your Personalized Learning Path
Here is your step-by-step learning path, strictly ordered to ensure all prerequisites are met logically:

Step 1: HTML & CSS
Category: Web Development
Prerequisites: None
Why it’s recommended: This is the starting point for all web development. It will teach you how to structure web pages (HTML5) and style them visually with responsive design (CSS3).
Step 2: JavaScript
Category: Web Development
Prerequisites: HTML & CSS (Completed in Step 1)
Why it’s recommended: JavaScript is the programming language of the web. It enables client-side interactivity, DOM manipulation, and asynchronous programming, forming the core of modern web applications.
Step 3: React
Category: Web Development
Prerequisites: JavaScript (Completed in Step 2)
Why it’s recommended: React is one of the most popular frontend libraries. Learning component-based architecture and hooks will allow you to build fast, modern, and scalable Single Page Applications (SPAs).
Step 4: Node.js
Category: Web Development
Prerequisites: JavaScript (Completed in Step 2)
Why it’s recommended: Node.js allows you to use JavaScript on the server side. Coupled with Express and React, it enables you to build full-stack JavaScript applications (MERN stack).
Step 5: MongoDB
Category: Database
Prerequisites: SQL (Satisfied by your profile)
Why it’s recommended: Since you already know SQL, adding NoSQL to your skill set gives you complete flexibility in handling modern web application data requirements, especially when building JavaScript/Node.js backends.
Step 6: FastAPI
Category: Backend
Prerequisites: Python Programming (Satisfied by your profile)
Why it’s recommended: Since you already know Python, FastAPI allows you to quickly build high-performance REST APIs. This gives you dual-backend capabilities (Node.js and Python), making you a versatile Web Developer.
Step 7: Git & GitHub
Category: Tools
Prerequisites: None
Why it’s recommended: Version control is non-negotiable for developers. It enables you to manage your code, collaborate with team members, and showcase your web development projects to recruiters via a public portfolio.
Step 8: Docker
Category: DevOps
Prerequisites: None
Why it’s recommended: Understanding containerization ensures that your web applications run consistently across development, staging, and production environments, making your deployment process smooth and professional.
Career Advice for an Aspiring Web Developer
Build Full-Stack Projects: Don’t just follow tutorials; create end-to-end projects. Combine React + Node.js + MongoDB for a JavaScript full-stack project, and React + FastAPI + SQL for a Python-based full-stack project.
Leverage Your Python & SQL Advantage: Many junior web developers only know basic frontend skills. Highlight your ability to construct robust backends with Python/FastAPI and manage relational/non-relational databases.
Showcase Code on GitHub: Make a habit of committing your code daily while taking the Git & GitHub course. A active GitHub contribution graph is an excellent visual proof of your consistency and technical growth to potential employers.
Deploy What You Build: Use Docker to containerize your applications and host them online. Having live, working URLs for your projects on your resume will set you apart from other candidates.

## Snapshots
<img width="1156" height="661" alt="image" src="https://github.com/user-attachments/assets/4dc75ce5-f88c-4577-a6bb-8a96e6755e27" />
<img width="948" height="619" alt="image" src="https://github.com/user-attachments/assets/b276abae-d280-4c3a-a08a-67ef085862ac" />
<img width="761" height="829" alt="image" src="https://github.com/user-attachments/assets/0d70aba4-ded8-446f-9f6c-b4f6c0a68357" />
<img width="787" height="778" alt="image" src="https://github.com/user-attachments/assets/daae6c2b-a340-49d0-8bda-10762bf23470" />




## Author
Sachin Kumbar
