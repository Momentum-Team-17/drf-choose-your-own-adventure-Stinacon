from django.shortcuts import render
from rest_framework import generics, filters, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, User, Author, Tracker
from .serializers import BookSerializer, TrackerSerializer
# Create your views here.


# create list of authors


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['featured']
    search_fields = ['title', 'author__name']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    # I want to write a conditional here the says if book they are entering has same author and name as existing book, give them an error message
    # something with request.data.get('title') and same with author
    # From chat GPT:
        # existing_book = Book.objects.filter(
        #     title=request.data.get('title'),
        #     author=request.data.get('author')
        # ).exists()

        # if existing_book:
        #     # If the book already exists, return a 400 Bad Request response with an error message
        #     return Response({'error': 'This book already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     # If the book does not exist, proceed with creating it
        #     return super().create(request, *args, **kwargs)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @permission_classes([IsAdminUser])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_classes([IsAdminUser])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @permission_classes([IsAdminUser])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserTracker(generics.ListCreateAPIView):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Tracker.objects.filter(user=self.request.user)
        return queryset
