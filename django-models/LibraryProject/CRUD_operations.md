from booksehlf.models import Book

new_book = Book(title="1984", author="George Orwell", publication_year=1949)
new_book.save()

the Book() command creates a book instance and assigns it to a variable named new_book, the save() commands his the database bysaving the new instance 


my_book = Book.objects.get(id=1)
my_book_title = my_book.title
my_book_author = my_book.author
my_book_pub_year = my_book.publication_year

the command Book.objects.get(id=1) retrieves the intance of the first book in the database and assigns specific attributes to variables listed beneath it 


my_book = Book.objects.get(title="1984")
my_book.title = "Nineteen Eighty-Four"

just like before, I got the instance of the model by querying for a particular column the title column and gave it a new name

my_book.delete()

this deletes the instance of the book model