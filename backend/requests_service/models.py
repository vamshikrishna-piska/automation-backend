from django.db import models
import uuid

class RequestModel(models.Model):
    STATUS_CHOICES=[
        ("PENDING","Pending"),
        ("PROCESSING","Processing"),
        ("COMPLETED","Completed"),
        ("FAILED","Failed"),
    ]

    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    request_type=models.CharField(max_length=50)
    payload=models.JSONField()
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
    error_message=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request_type} - {self.status}"