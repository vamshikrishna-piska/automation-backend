from celery import shared_task
from .models import RequestModel
from .services import RequestServices

@shared_task
def process_request_task(request_id):
    try:
        requestObj=RequestModel.objects.get(id=request_id)
    except RequestModel.DoesNotExist:
         return f"Request {request_id} not found"
    RequestServices.status_processing(requestObj)
    return f"Task completed for request {request_id}"