from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(read_only=True)
    class Meta:
        model = Todo
        fields = ("id", "task", "completed", "created_at", "modified_at", 'order')