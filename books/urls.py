from django.urls import path
from books.views import books_view

urlpatterns = [
    path('index', books_view),
]