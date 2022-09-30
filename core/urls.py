from turtle import clear
from django.urls import path
from .views import TodoListAPIView, TodoDetailAPIView
from users.views import UserDetailAPIView

urlpatterns = [
    path('todos/', TodoListAPIView.as_view(), name="todo_list"),
    path('todos/<pk>/', TodoDetailAPIView.as_view(), name="todo_detail"),
    path('users/me/', UserDetailAPIView.as_view(), name="user_detail"),
]