from django import forms
from books.models import ClubHouseRoom, Book


class ClubHouseRoomForm(forms.ModelForm):
    class Meta:
        fields = ['room_name']
        model = ClubHouseRoom


class BookForm(forms.ModelForm):
    class Meta:
        fields = ['author', 'title', 'cover']
        model = Book
