from django.db import models

# Create your models here.

class ModelTasks(models.Model):
    label = models.CharField(max_length = 150)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.label
    