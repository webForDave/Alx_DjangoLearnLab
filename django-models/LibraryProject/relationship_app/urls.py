from django.urls import path
from .views import all_books, BookDetail

urlpatterns = [
    path("books/", all_books, name="Books"),
    path("books/<int:pk>/", BookDetail.as_view(), name="Book detail"),
]
