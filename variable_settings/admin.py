from django.contrib import admin
from .models import Setting

class SettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

admin.site.register(Setting, SettingAdmin)