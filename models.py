from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    ava = models.ImageFiels()
    status = models.TextField()
    country = models.CharField(max_width=50)
    town = models.CharField(max_width=50)
    subscriptionsStatus = models.BooleanField()