# To start fast api server
# uvicorn main:app --reload

from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from emotion_analysis.emotion_model import EmotionModel

app = FastAPI()

# Allow CORS from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Emotion(BaseModel):
    emotionname: str
    id: int

@app.post("/emotions/")
def read_emotion(emotion: Emotion):
    emotion = emotion.dict()
    print("\n\n\n data",emotion)
    model = EmotionModel()
    prediction = model.process_review(emotion['emotionname'])
    print(prediction)
    return prediction