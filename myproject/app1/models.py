from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)