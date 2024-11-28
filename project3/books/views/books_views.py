from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Books
from django.views import View
import json

class GetAllBooks(View):
    # login_url = '/books/login',
    def get(self, request):
        books = Books.objects.all()  # Query to get all books
        # book_list = list(books.values())
        # return JsonResponse(book_list, safe=False)
        context = {
            'books': books  # Passing the books queryset to the template
        }
        return render(request, 'allbooks.html', context)
@method_decorator(csrf_exempt, name='dispatch')  # Apply csrf_exempt 
class AddBook(View):
    # login_url = '/books/login'
    def post(self, request):
        try:
            data = json.loads(request.body)  # Parse JSON request body
            title = data.get('title')
            author = data.get('author')
            pages = data.get('pages')

            new_book = Books(title=title, author=author, pages=pages)
            new_book.save()

            response_data = {
                'id': new_book.id,
                'title': new_book.title,
                'author': new_book.author,
                'pages': new_book.pages,
            }

            return JsonResponse(response_data, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)