from django.db import models

# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=50)
    uplolad_component = models.FileField(upload_to='Component/')
    
def Default():
        return {'Admin': 'password: 12345 email:ojudsonleo@gmail.com'}
    
class Json(models.Model):
    json = models.JSONField("Json", default=Default)
    #https://youtu.be/8tVoq291aZ8?list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&t=327q        