from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from todo.views import RegisterView  # або ім'я вашого класу реєстрації

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
# Вхід
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Вихід
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Реєстрація
    path('register/', RegisterView.as_view(), name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]

