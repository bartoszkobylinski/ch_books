from django.db import models


class ClubHouseRoom(models.Model):
    room_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.room_name}"


class Book(models.Model):
    room = models.ForeignKey(
        ClubHouseRoom, on_delete=models.CASCADE)
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    cover = models.FileField(upload_to='covers/')

    def __str__(self):
        return f"{self.title} by {self.author}"
