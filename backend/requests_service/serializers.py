from rest_framework import serializers
from requests_service.models import RequestModel
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user
    

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=RequestModel
        fields=["id","request_type","payload","status","error_message","created_at"]
        read_only_fields=["id","status","created_at"]


