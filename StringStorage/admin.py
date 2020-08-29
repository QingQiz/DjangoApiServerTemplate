from django.contrib import admin
from .models import StringStorage


@admin.register(StringStorage)
class ApiKeyAdmin(admin.ModelAdmin):
    pass
