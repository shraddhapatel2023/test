from pydantic import BaseModel


class Entity(BaseModel):
    text: str
    label: str


class EntityRecognitionRequest(BaseModel):
    text: str
