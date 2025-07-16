from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

def list_books(request):
    context = {"books": Book.objects.all()}
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    template_name = "relationship_app/library_detail.html"
    model = Library
