from django.urls import path
from . import views


app_name = "todo"

urlpatterns = [
    path('', views.todoView, name='todo-view'), 
    path('delete/<int:pk>/', views.deleteTodo, name='delete-todo'),
    path('update/<int:pk>/', views.updateTodo, name='update-todo'),
     
    
]