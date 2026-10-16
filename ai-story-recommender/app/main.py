from fastapi import FastAPI
from pydantic import BaseModel

from app.recommender.engine import RecommendationEngine

app = FastAPI(title="AI Story Recommender", version="0.1.0")
engine = RecommendationEngine()


class UserRequest(BaseModel):
    user_id: str
    interests: list[str] = []


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/recommend")
def recommend(request: UserRequest):
    return {
        "user_id": request.user_id,
        "recommendations": engine.recommend(request.interests),
    }
