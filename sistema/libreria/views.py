from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'page_libreria/home.html')

def uspage(request):
    return render(request, 'page_libreria/us.html')

def books(request):
    return render(request, 'books/index.html')

def create_book(request):
    return render(request, 'books/create.html')

def update_book(request):
    return render(request, 'books/update.html')