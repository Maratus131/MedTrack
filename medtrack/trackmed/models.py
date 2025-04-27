from django.db import models
from django.urls import reverse


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('user',kwargs ={'username':self.username})

    def __str__(self):
        return self.username