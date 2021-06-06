from django.db import models

# Create your models here.
class share(models.Model):
    sharefile = models.FileField(upload_to="share/")    