from django.contrib import admin
from .models import Notebook


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status")
    list_filter = ("user", "status", "timestamp")
