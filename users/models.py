from django.db import models
from djongo import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class usersDatabase(models.Model):
    Gender = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    _id=models.ObjectIdField()
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    DOB=models.DateField()
    Gender=models.CharField(max_length=10,choices=Gender,default="Male")
    salt=models.BinaryField(max_length=100)
    hash=models.BinaryField(max_length=100)

class Expense(models.Model):
    _id=models.ObjectIdField()
    Userid=models.TextField()
    Amount = models.FloatField()
    Remark = models.TextField()
    Type = models.TextField()
    Category    = models.TextField()

# Create your models here.
