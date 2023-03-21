from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Book(models.Model):
    CHOICES = (
        ('self-help', 'Self-Help'),
        ('graphic', 'Graphic Novel'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('comedy', 'Comedy'),
        ('spy', 'Spy'),
    )

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        to='Author', on_delete=models.CASCADE, related_name='books_by_author')
    date_published = models.DateField(blank=True, null=True)
    genre = models.CharField(choices=CHOICES, max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=100)
