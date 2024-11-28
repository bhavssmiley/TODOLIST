from django.db import models

# Create your models here.
class List(models.Model):
    taskname = models.CharField(max_length=100)
    taskdesc = models.CharField(max_length=200)
class List1(models.Model):
    taskname = models.CharField(max_length=100)
    taskdesc = models.CharField(max_length=200)
    
