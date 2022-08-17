from django.contrib import admin
from .models import *


class UrlAdmin(admin.ModelAdmin):
   list_display =("id","original_url","short_url")
   ordering =["id"]


admin.site.register(Url,UrlAdmin)
