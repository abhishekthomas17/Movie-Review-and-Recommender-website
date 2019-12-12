from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.movie)


admin.site.register(models.review)
