"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from todoapp import views as todo_views
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.task_list, name='task_list'),
    path('add_task/', todo_views.add_task, name='add_task'),
    path('delete_task/<int:i>', todo_views.delete_task, name='delete_task'),
    path('delete_all_tasks/', todo_views.delete_all_tasks, name='delete_all_tasks'),
    path('done_task/<int:i>', todo_views.done_task, name='done_task'),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
