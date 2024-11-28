from django.urls import path
from . import views
from .views.index_views import IndexView
from .views.books_views import GetAllBooks, AddBook
from .views.review_views import AddReview, GetReview
from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth_views import Register, LoginUser
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('get_all_books/', GetAllBooks.as_view(), name='get_all_books'),
    path('add_book/', AddBook.as_view(), name='add_book'),
    path('add_reviews/', AddReview.as_view(), name='add_reviews'),
    path('get_reviews/', GetReview.as_view(), name='get_reviews'),

    path('register/', Register.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
