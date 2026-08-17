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

## Author

Sachin Kumbar