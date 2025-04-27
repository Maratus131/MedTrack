from django.db import models

class User(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
