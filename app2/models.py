import email
from django.db import models

# Create your models here.

class student(models.Model):
    sname=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    jdate=models.DateField()

