from pydantic import BaseModel


class Service(BaseModel):
    name: str
    url: str
