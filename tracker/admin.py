from django.contrib import admin
from tracker.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("id", "name", "is_done", "created_at")
    list_display_links = ('id', 'name')
    list_filter = ("is_done", 'created_at')
