from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Todo
        fields = ['task', 'is_done', 'date', 'completed']
