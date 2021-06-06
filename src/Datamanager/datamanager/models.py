from django.db import models

# Create your models here.
class database_uploader(models.Model):
    upload_database = models.FileField()
    
class database_Writer(models.Model):
    write_data = models.TextField()