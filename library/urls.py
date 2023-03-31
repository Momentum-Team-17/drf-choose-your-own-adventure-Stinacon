from django.urls import path
from library import views


urlpatterns = [
    path('library/', views.BookList.as_view()),
    path('library/<int:pk>/', views.BookDetail.as_view()),
    path('tracker/', views.UserTracker.as_view()),
]
