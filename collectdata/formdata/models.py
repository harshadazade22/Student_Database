from django.db import models

# Create your models here.
class Saveform(models.Model):
    name=models.CharField(max_length=50,default=None)
    email=models.CharField(max_length=50,default=None)
    moblie=models.CharField(max_length=50,default=None)
    address=models.CharField(max_length=500,default=None)


