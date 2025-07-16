from django.shortcuts import render
from .models import Book

def all_books(request):
    context = {"books": Book.objects.all()}
    return render(request, "relationship_app/list_books.html", context)