from django.urls import path

from Books.book_app.views import index

urlpatterns = (
    path('', index, name='index book'),
)