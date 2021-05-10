from django.urls import path
from books.views import book_insert_view, IndexView

urlpatterns = [
    path('insert_book', book_insert_view),
    path('', IndexView.as_view())
]