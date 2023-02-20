from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    job = models.CharField(max_length=50)
