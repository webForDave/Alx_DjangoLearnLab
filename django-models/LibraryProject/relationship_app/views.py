from django.shortcuts import render
from .models import Book, Library
from django.views import generic

def all_books(request):
    context = {"books": Book.objects.all()}
    return render(request, "relationship_app/list_books.html", context)

class BookDetail(generic.DetailView):
    template_name = "relationship_app/library_detail.html"
    model = Library
