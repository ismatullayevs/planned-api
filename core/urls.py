from turtle import clear
from django.urls import path
from .views import TodoListAPIView, TodoDetailAPIView, clear_completed

urlpatterns = [
    path('todos/', TodoListAPIView.as_view(), name="todo_list"),
    path('todos/clear-completed/', clear_completed, name="clear_completed"),
    path('todos/<pk>/', TodoDetailAPIView.as_view(), name="todo_detail"),
]