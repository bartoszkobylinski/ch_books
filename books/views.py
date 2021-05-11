from django.shortcuts import render
from django.views.generic import TemplateView
from books.models import Book
from books.forms import ClubHouseRoomForm, BookForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


def book_insert_view(request):
    if request.method == "POST":
        clubhouse_room_form = ClubHouseRoomForm(request.POST)
        book_form = BookForm(request.POST)
        if clubhouse_room_form.is_valid() and book_form.is_valid():
            clubhouse_room_form.save()
            book_form.save()
        return render(request, 'index.html')
    else:
        clubhouse_room_form = ClubHouseRoomForm()
        book_form = BookForm()
        context = {'ch_room_f': clubhouse_room_form, 'book_f': book_form}
        return render(request, 'index.html', context=context)
