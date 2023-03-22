from django.shortcuts import render
from rest_framework import generics
from .models import Book, User, Author, Tracker
from .serializers import BookSerializer
# Create your views here.

# create list of authors


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
