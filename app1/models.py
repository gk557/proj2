import email
from pyexpat import model
from django.db import models

# Create your models here.
class student(models.Model):
    sname = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    jdate = models.DateField()
    phnumber = models.IntegerField(max_length=10, null=True)
