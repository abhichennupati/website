from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os
from html_helpers import get_main_html

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

app = FastAPI()

@app.get("/thought/{thought}")
async def thought(thought: str):
    print(thought)
    statement = text("""INSERT INTO thoughts(text) VALUES(:text)""")
    with engine.begin() as con:
        con.execute(statement, {"text": thought})

@app.get("/")
async def home():
    return HTMLResponse(content=get_main_html())
