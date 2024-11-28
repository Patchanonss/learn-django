from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from ..models import Books,Review
from django.views import View
import json

@method_decorator(csrf_exempt, name='dispatch')  # Apply csrf_exempt 
class AddReview(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            text = data.get('review_text')
            rating = data.get('rating')
            book_id = data.get('books_id')
            try:
                book = Books.objects.get(id=book_id)
            except Books.DoesNotExist:
                return JsonResponse({'error': 'Book not found'}, status=404)
            new_review = Review(review_text=text,rating=rating,book=book)
            new_review.save()
            response_data = {
                'id': new_review.id,
                'review_text': new_review.review_text,
                'rating': new_review.rating,
                'created_at' : new_review.created_at,
                'book' : {
                    'id': new_review.book.id,  # Serialize book object
                    'title': new_review.book.title,  # Add other fields as needed
                    'author' : new_review.book.author,
                    'pages' : new_review.book.pages
                }
            }
            return JsonResponse(response_data, status=201)  # Return
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

class GetReview(View):
    def get(self,request):
        try:
            book = Books.objects.all()
            reviews = book.reviews.all()
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)