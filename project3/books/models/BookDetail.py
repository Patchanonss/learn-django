from django.db import models
from .Books import Books
# Create your models here.
class BookDetail(models.Model):
    book = models.OneToOneField(Books, on_delete=models.CASCADE, related_name='detail')
    synopsis = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return f'Details for {self.book.title}'