from django.db import models

# Create your models here.
class Share(models.Model):
    comment = models.CharField(max_length=100)
    Share = models.FileField(upload_to="sharedFiles")