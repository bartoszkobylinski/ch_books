from django.urls import path
from books.views import book_insert_view, IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('insert_book', book_insert_view),
    path('', IndexView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
