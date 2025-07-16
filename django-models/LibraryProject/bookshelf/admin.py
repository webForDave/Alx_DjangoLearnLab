from django.contrib import admin
from .models import Book

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year",)
    list_filter = ("title",)
    search_fields = ("author", "publication_year",)

admin.site.register(Book, CustomUserAdmin)