from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ToDo(models.Model):
    content = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.localtime(timezone.now()))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    def __str__(self):
        return self.content
