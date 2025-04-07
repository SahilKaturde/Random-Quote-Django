from django.contrib import admin
from .models import Data

class AdminData(admin.ModelAdmin):
    list_display = ('id', 'quote')

admin.site.register(Data, AdminData)