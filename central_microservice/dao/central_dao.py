import pymongo

from central_microservice.enum.http_enum import HttpStatusCodeEnum
from services.response_services import AppServices

response_service = AppServices()
# MongoDB setup
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["service_registry_db"]
services_collection = db["services"]


class CentralDao:
    @staticmethod
    def insert_services(service):
        try:
            data = {"name": service.name, "url": service.url}
            result = services_collection.insert_one(data)
            return data
        except Exception as e:
            response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                     success=False,
                                                     message="Something Went Wrong!",
                                                     data=[])
            return response

    @staticmethod
    def get_services(service_name=None, flag=None):
        try:
            if flag:
                service_list = list(services_collection.find({}, {"_id": 0}))
                return service_list
            service_one = services_collection.find_one({"name": service_name})
            return service_one
        except Exception as e:
            response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                     success=False,
                                                     message="Something Went Wrong!",
                                                     data=[])
            return response
