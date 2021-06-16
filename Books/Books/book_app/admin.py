from django.contrib import admin

# Register your models here.
from Books.book_app.models import BookModel

admin.site.register(BookModel)