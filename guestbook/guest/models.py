from django.db import models

# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=100)

    