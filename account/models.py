from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser): #django에서 제공하는 로그인 및 로그아웃 클래스를 상속받는다.
    #내가 만들 모델에 추가하고 싶은 항목들만 적으면 된다.
    nickname = models.CharField(max_length=100) 
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)