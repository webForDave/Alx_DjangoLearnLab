from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register_view, list_books, LibraryDetailView, CustomLoginView

urlpatterns = [
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),    
    path("register/", register_view, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("books/", list_books, name="list_books"),
    path("books/<int:pk>/", LibraryDetailView.as_view(), name="Book detail"),
]
