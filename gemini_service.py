from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def get_gemini_response(user_input, task):

    prompts = {

        "ask": f"""
Answer the following educational question clearly.

Question:
{user_input}
""",

        "explain": f"""
Explain the following concept in simple language with an example.

Concept:
{user_input}
""",

        "quiz": f"""
Generate exactly 5 multiple-choice questions on the topic:

{user_input}

Return ONLY valid JSON.

Format:

[
  {{
    "question": "What is Python?",
    "options": [
      "Snake",
      "Programming Language",
      "Database",
      "Operating System"
    ],
    "correct": 1
  }}
]

Rules:
- Exactly 5 questions.
- Exactly 4 options per question.
- "correct" must be the option index (0-3).
- Return ONLY JSON.
- Do NOT use markdown.
""",

        "summary": f"""
Summarize the following educational content into bullet points.

Text:
{user_input}
""",

        "learning": f"""
Create a beginner-to-advanced learning roadmap for:

{user_input}
"""

    }

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompts[task]
        )

        return response.text

    except Exception as e:
        return f"ERROR: {e}"