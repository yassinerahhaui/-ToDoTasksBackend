from rest_framework import serializers
from .models import ModelTasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTasks
        fields = ['id', 'label', 'completed']