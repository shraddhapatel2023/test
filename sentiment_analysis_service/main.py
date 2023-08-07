import uvicorn
from fastapi import FastAPI

from sentiment_analysis_service.controller.sentiment_controller import sentiment_router

app = FastAPI()

if __name__ == "__main__":
    app.include_router(sentiment_router)
    uvicorn.run(app, host="localhost", port=8001, log_level="info")

    print("running")
