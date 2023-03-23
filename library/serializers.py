from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User, Book, Author, Tracker


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


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fileds = ('name',)


class TrackerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracker
        fields = (
            'user',
            'book',
            'status',
        )
