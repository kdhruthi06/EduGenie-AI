# EduGenie – Google Gemini Powered Learning Assistant

EduGenie is an AI-powered educational assistant that helps students learn more effectively through intelligent question answering, concept explanation, quiz generation, text summarization, and personalized learning recommendations. The application is built using FastAPI, Google Gemini, HTML, CSS, and Jinja2.

## 📺 Demo Video

> Add your demo video link here after recording.
https://github.com/kdhruthi06/EduGenie-AI/blob/main/Video%20Project.mp4

---

## 🚀 Features

- 🤖 **AI Question Answering** – Get accurate answers to educational questions using Google Gemini.
- 📚 **Concept Explanation** – Receive simple explanations with examples for difficult topics.
- 📝 **Quiz Generator** – Generate multiple-choice quizzes for any subject.
- 📄 **Text Summarizer** – Convert lengthy educational content into concise summaries.
- 🛣️ **Learning Path Generator** – Get a beginner-to-advanced roadmap for learning any topic.
- 🎨 **Interactive Dashboard** – User-friendly interface built using HTML, CSS, and Jinja2.
- ⚡ **FastAPI Backend** – High-performance backend for handling AI requests.

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Google Gemini API
- HTML
- CSS
- Jinja2
- JSON
- Uvicorn

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/EduGenie.git
```

### 2. Navigate to Project Folder

```bash
cd EduGenie
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API Key

Create a file named `config.py`

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

### 7. Run the Application

```bash
uvicorn app:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

---

## 📂 Project Structure

```
EduGenie/
│── app.py
│── config.py
│── requirements.txt
│── templates/
│── static/
│── services/
│── utils/
│── data/
```

---

## 📌 Future Enhancements

- User Authentication
- PDF Upload & Summarization
- Voice Assistant
- Progress Tracking
- Database Integration
- Multi-language Support

---

## 👨‍💻 Author

**K Dhruthi**

B.Tech CSE (AI & ML)
