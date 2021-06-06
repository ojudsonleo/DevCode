from django.db import models

# Create your models here.
class package(models.Model):
    command = models.CharField(max_length=60)