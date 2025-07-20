from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views, admin_view, librarian_view, member_view

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("books/", views.list_books, name="list_books"),
    path("books/<int:pk>/", views.LibraryDetailView.as_view(), name="Book detail"),
    path('admin-dashboard/', admin_view.admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view.librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_view.member_dashboard, name='member_dashboard'),
    path("books/add_book/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit_book/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
