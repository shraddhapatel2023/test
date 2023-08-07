from fastapi import APIRouter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from sentiment_analysis_service.dto.sentiment_dto import SentimentAnalysisRequest
from sentiment_analysis_service.enum.http_enum import HttpStatusCodeEnum
from sentiment_analysis_service.service.sentiment_service import SentimentService
from services.response_services import AppServices

response_service = AppServices()
sentiment_router = APIRouter()

sia = SentimentIntensityAnalyzer()


@sentiment_router.post("/analyze")
async def analyze_sentiment(request: SentimentAnalysisRequest):
    try:
        text_data = request.text
        response = SentimentService.analyze_sentiment_service(text_data)
        return response
    except Exception as e:
        response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                 success=False,
                                                 message="Something Went Wrong!",
                                                 data=[])
        return response
