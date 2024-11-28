from django.db import models
from .BookGenre import BookGenre
# Create your models here.
class Books(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField()
    genres = models.ManyToManyField(BookGenre, related_name='books')

    def __str__(self):
        return f'title : {self.title} | author : {self.author}'