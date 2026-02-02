from rest_framework import serializers
from requests_service.models import RequestModel

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=RequestModel
        fields=["id","request_type","payload","status","error_message","created_at"]
        read_only_fields=["id","status","created_at"]

        

