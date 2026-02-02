from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from requests_service.models import RequestModel
from requests_service.serializers import RequestSerializer
from requests_service.services import RequestServices
from requests_service.process import process_request


class Request_POSTAPI(APIView):
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            object = serializer.save(status="PENDING")
            result = RequestServices.status_processing(object)
            return Response(
                {"request_id": object.id,"status": object.status,"preview": result,},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Request_GETAPI(APIView):
    def get(self,pk):
        object=RequestModel.objects.get(pk=pk)

        return Response({
         "request_id":object.id,
         "request_type":object.request_type,
         "status":object.status,
         "error_message":object.error_message,
         "created_at":object.created_at,
         "updated_at":object.updated_at   
        })