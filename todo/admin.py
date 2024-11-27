
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at')  # Замість цих полів вкажіть поля вашої моделі
    list_filter = ('completed', 'created_at')  # Фільтри за статусом виконання і датою створення
    search_fields = ('title', 'description')  # Пошук за назвою і описом
