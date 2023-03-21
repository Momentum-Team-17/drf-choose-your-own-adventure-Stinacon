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
