from django.shortcuts import render
from ..models import Books
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        book1 = Books(title="The Great Gatsby", author="F. Scott Fitzgerald", pages=180)
        book_dto = {
            "title": book1.title,
            "author": book1.author,
            "pages": book1.pages
        }
        return render(request, 'index.html', {'book': book_dto})