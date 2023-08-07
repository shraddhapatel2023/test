import spacy

from entity_recognition_service.dto.entity_dto import Entity
from entity_recognition_service.enum.http_enum import HttpStatusCodeEnum
from services.response_services import AppServices

response_service = AppServices()
# Load the medium English model
nlp = spacy.load("en_core_web_md")


class EntityService:
    @staticmethod
    def entity_recog_service(EntityRecognitionRequest):
        try:
            text_data = EntityRecognitionRequest.text
            doc = nlp(text_data)

            # Tokenization
            tokens_data = [token.text for token in doc]

            # Named Entity Recognition (NER)
            entities = [Entity(text=ent.text, label=ent.label_) for ent in doc.ents]
            if entities:
                response = response_service.app_response(status_code=HttpStatusCodeEnum.OK,
                                                         success=True,
                                                         message="Entity Fetched Successfully!!",
                                                         data=[{"entities": entities}])

                return response

            response = response_service.app_response(status_code=HttpStatusCodeEnum.NOT_FOUND,
                                                     success=False,
                                                     message="Entity Not Found Please Try again!!",
                                                     data=[])
            return response
        except Exception as e:
            response = response_service.app_response(status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR,
                                                     success=False,
                                                     message="Something went wrong!!",
                                                     data=[])
            return response
