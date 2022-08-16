from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.uspage, name='uspage'),
    path('libros/', views.books, name='books'),
    path('libros/crear/', views.create_book, name='create_book'),
    path('libros/editar/', views.update_book, name='update_book'),

]
