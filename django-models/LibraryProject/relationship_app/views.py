from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("list_books")
        else:
            messages.error(request, "Invalid username pr password")
            return render(request, "relationship_app/login.html", {})

    return render(request, "relationship_app/login.html", {})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect("login")

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get("username") 
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username:
            messages.error(request, "A username must be given")
            return render(request, "relationship_app/register.html")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "relationship_app/register.html")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return render(request, "relationship_app/register.html")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "relationship_app/register.html")
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect("list_books")

    else:
        return render(request, "relationship_app/register.html", {})

def list_books(request):
    context = {"books": Book.objects.all()}
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    template_name = "relationship_app/library_detail.html"
    model = Library

