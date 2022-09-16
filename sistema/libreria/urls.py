from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros/', views.uspage, name='uspage'),
    path('libros/', views.books, name='books'),
    path('libros/crear/', views.create_book, name='create_book'),
    path('libros/editar/<int:id>/', views.update_book, name='update_book'),
    path('libros/eliminar/<int:id>/', views.delete_book, name='delete_book'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

