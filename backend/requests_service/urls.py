from django.urls import path
from requests_service.views import Request_GETAPI,Request_POSTAPI,RegisterView

urlpatterns = [
    path("register/",RegisterView.as_view(),name='register'),
    path("requests/",Request_POSTAPI.as_view(),name='create_request'),
    path("requests/<uuid:pk>/",Request_GETAPI.as_view(),name='request_details'),
    ]
