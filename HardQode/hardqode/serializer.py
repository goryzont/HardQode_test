from rest_framework import serializers, viewsets
from .models import Product, Lesson


class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'cost', 'lesson_count']

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_link']


