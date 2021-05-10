from django.shortcuts import render
from books.forms import ClubHouseRoomForm, BookForm


def books_view(request):
    clubhouse_room_form = ClubHouseRoomForm()
    book_form = BookForm()
    context = {
        'ch_room_f' : clubhouse_room_form,
        'book_f' : book_form
    }
    return render(request, 'index.html', context=context)
