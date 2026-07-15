from utils.storage import save_json
from services.gemini_service import get_gemini_response
from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"request": request}
    )

@app.get("/ask")
def ask_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="ask.html",
        context={"request": request, "response": None}
    )


@app.post("/ask")
def ask_ai(request: Request, question: str = Form(...)):

    answer = get_gemini_response(question, "ask")
    save_json(
    "queries.json",
    {
        "feature": "Ask AI",
        "query": question
    }
    )

    save_json(
        "responses.json",
        {
            "feature": "Ask AI",
            "response": answer
        }
    )
    return templates.TemplateResponse(
        request=request,
        name="ask.html",
        context={
            "request": request,
            "response": answer
        }
    )   


@app.get("/explain")
def explain_page(request: Request):

    return templates.TemplateResponse(

        request=request,

        name="explain.html",

        context={"request":request,"response":None}

    )


@app.post("/explain")
def explain(request: Request, concept: str = Form(...)):

    answer = get_gemini_response(concept, "explain")
    save_json(
    "queries.json",
    {
        "feature":"Explain",
        "query":concept
    }
    )

    save_json(
        "responses.json",
        {
            "feature":"Explain",
            "response":answer
        }
    )
    return templates.TemplateResponse(

        request=request,

        name="explain.html",

        context={

            "request":request,

            "response":answer

        }

    )
    

@app.get("/quiz")
def quiz_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="quiz.html",
        context={
            "request": request,
            "response": None
        }
    )


@app.post("/quiz")
def quiz(request: Request, topic: str = Form(...)):

    try:

        quiz_text = get_gemini_response(topic, "quiz")

        # If Gemini returned an error
        if quiz_text.startswith("ERROR:"):
            return templates.TemplateResponse(
                request=request,
                name="quiz.html",
                context={
                    "request": request,
                    "error": quiz_text
                }
            )

        quiz_text = quiz_text.strip()

        if quiz_text.startswith("```json"):
            quiz_text = quiz_text.replace("```json", "", 1)

        if quiz_text.endswith("```"):
            quiz_text = quiz_text[:-3]

        quiz_text = quiz_text.strip()

        quiz = json.loads(quiz_text)

        save_json(
            "quizzes.json",
            {
                "topic": topic,
                "quiz": quiz
            }
        )

        return templates.TemplateResponse(
            request=request,
            name="quiz.html",
            context={
                "request": request,
                "quiz": quiz
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            request=request,
            name="quiz.html",
            context={
                "request": request,
                "error": str(e)
            }
        )


@app.get("/summary")
def summary_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="summary.html",
        context={
            "request": request,
            "response": None
        }
    )


@app.post("/summary")
def summary(request: Request, text: str = Form(...)):

    answer = get_gemini_response(text, "summary")
    save_json(
    "summaries.json",
    {
        "text":text,
        "summary":answer
    }
    )
    return templates.TemplateResponse(
        request=request,
        name="summary.html",
        context={
            "request": request,
            "response": answer
        }
    )


@app.get("/learning")
def learning_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="learning.html",
        context={
            "request": request,
            "response": None
        }
    )


@app.post("/learning")
def learning(request: Request, topic: str = Form(...)):

    answer = get_gemini_response(topic, "learning")
    save_json(
    "learning_paths.json",
    {
        "topic":topic,
        "roadmap":answer
    }
    )
    return templates.TemplateResponse(
        request=request,
        name="learning.html",
        context={
            "request": request,
            "response": answer
        }
    )