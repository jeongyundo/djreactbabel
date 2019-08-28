from django.db import models
from django.contrib.auth.models import User
#auth.models를 호출해 사용자 정보 등록기능을 추가

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(
        User, related_name="leads", on_delete=models.CASCADE, null=True)
    #owner에 사용자 정보 추가
    created_at = models.DateTimeField(auto_now_add=True)
