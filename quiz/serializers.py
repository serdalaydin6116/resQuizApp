from rest_framework import serializers
from .models import (
    Category,
    Quiz,
    Question,
    Option
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category(
            'id',
            'name',
            'quiz_count',
        )