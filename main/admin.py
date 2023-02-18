from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'task_name', 'task_create', 'is_complete'
    ]

    list_display_links = [
        'task_name'
    ]

    list_filter = [
        'user', 'is_complete'
    ]

    list_per_page = 25


admin.site.register(Task, TaskAdmin)