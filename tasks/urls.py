from django.urls import path
from .views import TaskListCreateView, TaskDetailView, RegisterView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='tasks_list'),
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='tasks_detail'),
    path('users/register/', RegisterView.as_view(), name='users_register'),
]
