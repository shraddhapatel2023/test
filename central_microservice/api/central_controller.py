import json

import httpx
from fastapi import APIRouter, HTTPException
from typing import Dict

from central_microservice.dao.central_dao import CentralDao
from central_microservice.dto.analysis_dto import Analysis
from central_microservice.dto.service_dto import Service
from central_microservice.enum.http_enum import HttpStatusCodeEnum
from central_microservice.service.central_service import CentralService
from services.response_services import AppServices

response_service = AppServices()
api_router = APIRouter()

# Sample data store to hold registered services (for in-memory storage)
services_registry: Dict[str, str] = {}
central_service = CentralService()


@api_router.post("/services/")
async def register_service(service: Service):
    try:
        Service.name = service.name
        Service.url = service.url
        response = central_service.register_service(Service)
        # Store the service in the in-memory registry as well for faster lookups
        services_registry[service.name] = service.url

        return response
    except Exception as e:
        response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                 success=False,
                                                 message="Something Went Wrong!",
                                                 data=[])
        return response


@api_router.get("/services/")
async def list_services():
    try:
        # Retrieve all services from MongoDB
        response = central_service.get_services()
        return response
    except Exception as e:
        response = response_service.app_response(status_code=500,
                                                 success=False,
                                                 message="Something Went Wrong!",
                                                 data=[])
        return response


@api_router.post("/analyze/")
async def analyze_text(request_data: Analysis):
    service_name = request_data.service
    text_data = request_data.text
    central_dao = CentralDao()

    # Check if the service name exists in MongoDB
    service_record = central_dao.get_services(service_name)

    if not service_record:
        raise HTTPException(status_code=404, detail="Requested service does not exist")

    service_url = service_record["url"]

    # Forward the request to the appropriate service using HTTP client (HTTPX)
    headers = {"Content-Type": "application/json"}  # Adjust headers if needed by the external service
    payload = json.dumps({"text": text_data})

    try:
        async with httpx.AsyncClient() as client:
            get_response_data = await client.post(service_url, headers=headers, data=payload)

            # Return get_response_data in json form
            response = get_response_data.json()

    except httpx.HTTPStatusError as e:
        error_message = f"External service returned HTTP error: {e}"
        response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                 success=False,
                                                 message=error_message,
                                                 data=[])
    return response
