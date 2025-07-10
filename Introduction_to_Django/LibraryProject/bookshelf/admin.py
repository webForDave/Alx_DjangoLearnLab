from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ("title", "author", "publication_year",)
    list_filter = ("title",)

admin.site.register(Book, CustomUserAdmin)