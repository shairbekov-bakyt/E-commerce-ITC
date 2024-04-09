from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    is_done = models.BooleanField()
    created_at = models.DateTimeField()


class TaskCopy(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    is_done = models.BooleanField()
    created_at = models.DateTimeField()