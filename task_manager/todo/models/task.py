from django.db import models
from django.conf import settings

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subtasks')
    tags = models.ManyToManyField('todo.Tag', blank=True, related_name='tasks')
    def __str__(self):
        return self.title
