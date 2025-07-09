from bookshelf.model import Book

my_book = Book.objects.get(title="1984")
my_book.delete()