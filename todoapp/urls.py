from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('insert_todo/', views.insert_todo, name='insert-todo'),
    path('delete_todo/<int:todo_id>', views.delte_todo_item, name='delete_todo_item'),
]