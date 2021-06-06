from django.db import models

# Create your models here.
class database(models.Model):
    database = models.CharField(max_length=50)
    database_upload = models.FileField()
    write_data = models.TextField(blank=True)
    