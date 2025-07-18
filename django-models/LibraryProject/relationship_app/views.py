from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import LoginView as DjangoLoginView

class CustomLoginView(DjangoLoginView):
    template_name = "relationship_app/login.html"

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect("login")

def register_view(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            return redirect("list_books")
    return render(request, "relationship_app/register.html", {"form": form})

def list_books(request):
    context = {"books": Book.objects.all()}
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    template_name = "relationship_app/library_detail.html"
    model = Library

