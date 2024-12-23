from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tags', null=True, blank=True)

    def __str__(self):
        return self.name
