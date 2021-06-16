from django.forms import ModelForm

from Books.book_app.models import BookModel


class BookModelForm(ModelForm):
    class Meta:
        book = BookModel
        fields = '__all__'
