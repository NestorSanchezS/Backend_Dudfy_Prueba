from django.contrib import admin

from tasks.models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "completed")


admin.site.register(Tasks, TasksAdmin)

