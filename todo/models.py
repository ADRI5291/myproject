from django.db import models
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tags = TaggableManager()  # Додаємо менеджер тегів
    def __str__(self):
        return self.title
    
class Task(models.Model):
    class Task(models.Model):
        STATUS_CHOICES = [
            ('pending', 'Очікує'),
            ('in_progress', 'Виконується'),
            ('completed', 'Завершено'),
        ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Додане поле
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=1)  # Зв'язок із користувачем

    def __str__(self):
        return self.title
