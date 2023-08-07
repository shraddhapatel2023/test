from fastapi import APIRouter

from entity_recognition_service.enum.http_enum import HttpStatusCodeEnum
from entity_recognition_service.service.entity_service import EntityService
from services.response_services import AppServices
response_service = AppServices()
import spacy

from entity_recognition_service.dto.entity_dto import EntityRecognitionRequest, Entity

# Load the medium English model
nlp = spacy.load("en_core_web_md")

entity_router = APIRouter()


@entity_router.post("/recognize")
async def analysis_entity_recognize(request: EntityRecognitionRequest):
    try:
        EntityRecognitionRequest.text = request.text
        response = EntityService().entity_recog_service(EntityRecognitionRequest)
        return response
    except Exception as e:
        response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                 success=False,
                                                 message="Something Went Wrong!",
                                                 data=[])
        return response


