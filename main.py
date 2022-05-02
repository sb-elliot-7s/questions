from fastapi import FastAPI
from question.controllers import question_router

app = FastAPI()
app.include_router(question_router)
