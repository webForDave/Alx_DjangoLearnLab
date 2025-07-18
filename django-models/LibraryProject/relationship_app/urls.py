from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, logout_view, list_books, LibraryDetailView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("books/", list_books, name="list_books"),
    path("books/<int:pk>/", LibraryDetailView.as_view(), name="Book detail"),
]
