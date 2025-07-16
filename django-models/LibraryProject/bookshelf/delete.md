from bookshelf.models import Book

my_book = Book.objects.get(title="1984")
my_book.delete()