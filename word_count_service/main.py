import uvicorn
from fastapi import FastAPI

from word_count_service.controller.word_count_controller import word_count_router

app = FastAPI()

if __name__ == "__main__":
    app.include_router(word_count_router)
    uvicorn.run(app, host="localhost", port=8002, log_level="info")
    print("running")
