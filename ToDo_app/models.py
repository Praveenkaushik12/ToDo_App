from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profession=models.CharField(max_length=100,default='Unspecified')
    


