from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
from Books.book_app.forms import BookModelForm
from Books.book_app.models import BookModel


def index(request):
    context = {
        'books': BookModel.objects.all()
    }
    return render(request, 'index.html', context)


def create(request):
    book = BookModel()
    if request.method == ("GET"):
        form = BookModelForm(instance=book)
        context = {
            'form': form,
        }
        return render(request, 'create.html', context)
    else:
        form = BookModelForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('index book')
        context = {
            'form': form
        }
        return render(request, f'create.html', context)


def edit(request, pk):
    book = BookModel.objects.get(pk=pk)
    if request.method == ("GET"):
        form = BookModelForm(instance=book)
        context = {
            'form': form,
        }
        return render(request, 'edit.html', context)
    else:
        form = BookModelForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('index book')
        context = {
            'form': form
        }
        return render(request, f'edit.html', context)
