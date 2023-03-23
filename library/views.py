from django.shortcuts import render
from rest_framework import generics, filters, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, User, Author, Tracker
from .serializers import BookSerializer
# Create your views here.


# create list of authors


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['featured']
    search_fields = ['title', 'author__name']


class BookDetail(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @permission_classes([IsAdminUser])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_classes([IsAdminUser])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
