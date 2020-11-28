
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),
]
