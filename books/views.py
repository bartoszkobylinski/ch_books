from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from books.models import ClubHouseRoom, Book
from books.forms import ClubHouseRoomForm, BookForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rooms = ClubHouseRoom.objects.all()
        print(type(rooms))
        for room in rooms:
            ch_room = {'room': room}
            print(f'to jest ch_room: {ch_room}')
            books = Book.objects.filter(**ch_room)
            for book in books:
                print(f"to jest book: {book}")
                print(f"to jest type {type(book)}")
            # print(f"a to jes queryset books{books}")
            # print(f"to jest typ {type(books)}")
            # context[room]
            
        # print(f"to jest context {context}")
        # context['books'] = Book.objects.all()
        return context




def book_insert_view(request):
    
    if request.method == "POST":
        clubhouse_room_form = ClubHouseRoomForm(request.POST, prefix='room_form')
        book_form = BookForm(request.POST,  prefix='book_form')
        print('aaaaa')
        print(request.body)
        print(f"that is author {type(request.body)}")
        if clubhouse_room_form.is_valid() and book_form.is_valid():
            print('dupa')
            print(request)
            clubhouse_room_form.save()
            book_form.save()
        return render(request, 'index.html')
        
    else:
        print('not valid')
        clubhouse_room_form = ClubHouseRoomForm()
        book_form = BookForm()
        context = {'ch_room_f': clubhouse_room_form,
            'book_f': book_form}
        return render(request, 'index.html', context=context)

    context = {
            'ch_room_f' : clubhouse_room_form,
            'book_f' : book_form
        }
    return render(request, 'index.html', context=context)
