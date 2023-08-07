from pydantic import BaseModel


class WordCountRequest(BaseModel):
    text: str
