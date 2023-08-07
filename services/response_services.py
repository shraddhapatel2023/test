class AppServices:
    @staticmethod
    def app_response(status_code: int, message: str, success: bool = None,
                     data: any = None) -> dict:
        response = {
            "status_code": status_code,
            "success": success,
            "message": message,
            "data": data
        }

        return response
