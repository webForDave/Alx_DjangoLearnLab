from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book, Library
from django.views.generic.detail import DetailView

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    return render(request, "relationship_app/register.html", {"form": form})

def list_books(request):
    context = {"books": Book.objects.all()}
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    template_name = "relationship_app/library_detail.html"
    model = Library
