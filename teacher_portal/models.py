from audioop import maxpp
import email
from pickle import TRUE
from django.db import models

# Create your models here.

class teacher(models.Model):
    tname = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    jdate = models.DateField()
    phnumber = models.IntegerField(max_length=10, null=TRUE)
 
    def __str__(self):
        return self.branch
        