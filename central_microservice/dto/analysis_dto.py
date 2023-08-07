from pydantic import BaseModel


class Analysis(BaseModel):
    service: str
    text: str
