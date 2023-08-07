import uvicorn
from fastapi import FastAPI
from entity_recognition_service.controller.entity_controller import entity_router

app = FastAPI()

if __name__ == "__main__":
    app.include_router(entity_router)
    uvicorn.run(app, host="localhost", port=8003, log_level="info")

    print("running")
