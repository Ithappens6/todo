from django.urls import path
from .views import RegisterView, LoginView
from .views import TaskListCreateView, TaskDetailView
from .views import TagListCreateView, TagDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail')
]
