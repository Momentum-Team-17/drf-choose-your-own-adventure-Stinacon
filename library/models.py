from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


class User(AbstractUser):
    pass


# add string methods for book and author models
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
        to='Author', on_delete=models.CASCADE)
    date_published = models.DateField(blank=True, null=True)
    genre = models.CharField(choices=CHOICES, max_length=50)
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['title', 'author'], name='constraints')
        ]

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tracker(models.Model):
    CHOICES = (
        ('want to read', 'Want to Read'),
        ('reading', 'Reading'),
        ('finished', 'Finished'),
    )

    user = models.ForeignKey(
        to='User', on_delete=models.CASCADE, related_name="trackings_of_user")
    book = models.ForeignKey(
        to='Book', on_delete=models.CASCADE, related_name="trackings_of_book")
    status = models.CharField(choices=CHOICES, max_length=50)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'book'], name='tracker_constraints')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}: {self.status}"
