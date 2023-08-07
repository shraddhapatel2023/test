from services.response_services import AppServices
from word_count_service.enum.http_enum import HttpStatusCodeEnum

response_service = AppServices()


class WordCountService:
    @staticmethod
    def word_count_service(word_count_dto):
        try:
            text_data = word_count_dto.text
            word_count = len(text_data.split())
            response = response_service.app_response(status_code=HttpStatusCodeEnum.OK,
                                                     success=True,
                                                     message="Word Count Fetched Successfully !!",
                                                     data=[{
                                                         "word_count": word_count
                                                     }])
            return response
        except Exception as e:
            response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                     success=False,
                                                     message="Something Went Wrong!",
                                                     data=[])
            return response
