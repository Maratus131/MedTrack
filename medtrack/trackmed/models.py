from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)