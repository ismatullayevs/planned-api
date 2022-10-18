from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField(read_only=True)
    class Meta:
        model = Todo
        fields = ("id", "uid", "task", "completed", "created_at", 'order')