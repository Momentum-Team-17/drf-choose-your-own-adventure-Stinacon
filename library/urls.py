from django.urls import path
from library import views


urlpatterns = [
    path('books/', views.BookList.as_view()),
]
