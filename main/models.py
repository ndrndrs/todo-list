from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    task_create = models.DateTimeField(auto_now_add=True)
    task_name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ['-is_complete']

