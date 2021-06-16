from django.urls import path

from Books.book_app.views import index, edit, create

urlpatterns = (
    path('', index, name='index book'),
    path('create/', create, name='create book'),
    path('edit/<int:pk>', edit, name='edit book'),
)