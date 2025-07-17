from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, register_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("books/", list_books, name="list_books"),
    path("books/<int:pk>/", LibraryDetailView.as_view(), name="Book detail"),
]
