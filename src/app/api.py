from fastapi import FastAPI
from pydantic import BaseModel

from ..tracker.analyze import analyze_text
from ..tracker.viz import plot_daily_trend

app = FastAPI(title="AI Mood Tracker API")


class Inp(BaseModel):
    text: str
    lang: str | None = None


@app.post("/analyze")
def analyze(inp: Inp):
    res = analyze_text(inp.text, inp.lang)
    plot_daily_trend()
    return res
