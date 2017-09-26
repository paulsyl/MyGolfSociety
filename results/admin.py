from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.User_Player_Link)
admin.site.register(models.Results)
