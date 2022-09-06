from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Notes)
admin.site.register(models.Assignments)
admin.site.register(models.Todo)