from django.contrib import admin
from .models import database_uploader, database_Writer

# Register your models here.
admin.site.register(database_uploader)
admin.site.register(database_Writer)