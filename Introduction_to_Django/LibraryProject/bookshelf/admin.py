from django.contrib import admin
from .models import Book

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year",)
    search_fields = ("title",)

admin.site.register(Book, CustomUserAdmin)