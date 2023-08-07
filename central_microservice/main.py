import uvicorn
from fastapi import FastAPI

from central_microservice.api.central_controller import api_router

service_app = FastAPI()

if __name__ == "__main__":
    service_app.include_router(api_router)
    uvicorn.run(service_app, host="localhost", port=8000, log_level="info")
    print("running")
