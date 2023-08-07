from fastapi import APIRouter

from services.response_services import AppServices
from word_count_service.enum.http_enum import HttpStatusCodeEnum

response_service = AppServices()
from word_count_service.dto.word_count_dto import WordCountRequest
from word_count_service.service.word_count_service import WordCountService

word_count_router = APIRouter()


@word_count_router.post("/count")
async def analyze_word_count(request: WordCountRequest):
    try:
        # Extract the text from the request
        WordCountRequest.text = request.text
        response = WordCountService().word_count_service(WordCountRequest)

        return response
    except Exception as e:
        response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                 success=False,
                                                 message="Something Went Wrong!",
                                                 data=[])
        return response
