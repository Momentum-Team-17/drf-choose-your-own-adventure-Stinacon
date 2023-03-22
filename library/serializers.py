from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User, Book, Author


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'date_published',
            'genre',
            'featured',
        )
