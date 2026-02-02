from requests_service.models import RequestModel
from requests_service.process import process_request

class RequestServices:
    @staticmethod
    def status_processing(request_object:RequestModel):
        if request_object.status!="PENDING":
            raise ValueError("Only pending requests can be processed.")
        request_object.status="PROCESSING"
        request_object.save(update_fields=["status","updated_at"])
        
        try:
            result = process_request(request_object.payload)
            request_object.status="COMPLETED"
            request_object.save(update_fields=["status","updated_at"])
            return result
        except Exception as e:
            request_object.status="FAILED"
            request_object.error_message=str(e)
            request_object.save(update_fields=["status","error_message","updated_at"])
            raise