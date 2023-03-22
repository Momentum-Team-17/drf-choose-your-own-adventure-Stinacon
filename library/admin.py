from django.contrib import admin
from .models import Book, Author, User, Tracker

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Tracker)
