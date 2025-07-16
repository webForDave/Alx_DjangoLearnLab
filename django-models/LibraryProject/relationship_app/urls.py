from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="Books"),
    path("books/<int:pk>/", LibraryDetailView.as_view(), name="Book detail"),
]
