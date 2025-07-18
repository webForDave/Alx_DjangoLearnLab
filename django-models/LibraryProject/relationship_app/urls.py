from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView
from .views import list_books, LibraryDetailView, login_view, register_view

urlpatterns = [
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),    
    path("register/", register_view, name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("books/", list_books, name="list_books"),
    path("books/<int:pk>/", LibraryDetailView.as_view(), name="Book detail"),
]
