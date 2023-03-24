from rest_framework import serializers
from .models import User, Book, Author, Tracker


class TrackerSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()

    class Meta:
        model = Tracker
        fields = (
            'id',
            'user',
            'book',
            'status',
        )


class UserSerializer(serializers.ModelSerializer):
    trackings_of_user = TrackerSerializer(
        many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'trackings_of_user',
        )


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
        fileds = ('id', 'name',)
