import json
from typing import Dict
from bson import json_util

from central_microservice.dao.central_dao import CentralDao
from central_microservice.enum.http_enum import HttpStatusCodeEnum
from services.response_services import AppServices

# Sample data store to hold registered services (for in-memory storage)
services_registry: Dict[str, str] = {}
central_dao = CentralDao()
response_service = AppServices()


class CentralService:
    @staticmethod
    def register_service(service):
        try:
            response = response_service.app_response(status_code=HttpStatusCodeEnum.OK,
                                                     success=True,
                                                     message="Service Already Exist!!",
                                                     data=[])

            result = central_dao.get_services(service.name)
            if result:
                return response
            result = central_dao.insert_services(service)
            result_data = json.loads(json_util.dumps(result))
            response = response_service.app_response(status_code=HttpStatusCodeEnum.CREATED,
                                                     success=True,
                                                     message="Service Inserted Successfully!",
                                                     data=result_data)
            return response
        except Exception as e:
            response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                     success=False,
                                                     message="Something Went Wrong!",
                                                     data=[])
            return response

    @staticmethod
    def get_services():
        try:
            result = central_dao.get_services(flag="all")
            if result:
                response = response_service.app_response(status_code=HttpStatusCodeEnum.OK,
                                                         success=True,
                                                         message="Fetched Services Successfully!",
                                                         data=result)
                return response
            else:
                response = response_service.app_response(status_code=HttpStatusCodeEnum.NOT_FOUND,
                                                         success=True,
                                                         message="No Data Found!",
                                                         data=[])
                return response
        except Exception as e:
            response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                     success=False,
                                                     message="Something Went Wrong!",
                                                     data=[])
            return response
