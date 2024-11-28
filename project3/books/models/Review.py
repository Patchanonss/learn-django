from django.db import models
from .Books import Books
# Create your models here.
    
class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.book.title} by {self.rating}'