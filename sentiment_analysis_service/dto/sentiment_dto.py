from pydantic import BaseModel


class SentimentAnalysisRequest(BaseModel):
    text: str
