from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from requests_service.models import RequestModel
from requests_service.serializers import RequestSerializer,RegistrationSerializer
from .tasks import process_request_task

class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"User registered successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




class Request_POSTAPI(APIView):
    permission_classes=[IsAuthenticated] #jwt
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            object = serializer.save(status="PENDING")
            process_request_task.delay(str(object.id))
            # result = RequestServices.status_processing(object)
            return Response(
                {"request_id": object.id,"status": "PENDING",},
                status=status.HTTP_202_ACCEPTED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Request_GETAPI(APIView):
    permission_classes=[IsAuthenticated] #jwt
    def get(self,request,pk):
        try:
            object=RequestModel.objects.get(pk=pk)
        except RequestModel.DoesNotExist:
            return Response(
                {"error":"Request not found."},status=status.HTTP_404_NOT_FOUND
            )

        return Response({
         "request_id":object.id,
         "request_type":object.request_type,
         "status":object.status,
         "error_message":object.error_message,
         "created_at":object.created_at,
         "updated_at":object.updated_at   
        })