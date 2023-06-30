from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    completed = models.BooleanField(default=False)
