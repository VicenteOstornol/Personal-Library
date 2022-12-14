from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from ipdb import set_trace
# Create your views here.

def index(request):
    return render(request, 'page_libreria/home.html')

def uspage(request):
    return render(request, 'page_libreria/us.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form__ = BookForm(request.POST or None, request.FILES or None)
        if form__.is_valid():
            form__.save()
            return redirect('books')

    else:
        form__ = BookForm()
    return render(request, 'books/create.html', {'form__': form__})

def update_book(request, id):
    book = Book.objects.get(id=id)
    form__ = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form__.is_valid():
        form__.save()
        return redirect('books')

    return render(request, 'books/update.html', {'form__': form__})



def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')