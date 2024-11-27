

from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import TaskForm  # Імпортуємо нашу форму

# Існуюча функція
def task_list(request):
    tasks = Task.objects.all()  # Отримання всіх завдань
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# Нова функція для створення завдань
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Повернення до списку завдань
    else:
        form = TaskForm()
    return render(request, 'todo/create_task.html', {'form': form})
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task

# Клас для створення завдання
class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed']  # Поля, які будуть у формі
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task_list')

# Клас для редагування завдання
class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task_list')

# Клас для видалення завдання
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
