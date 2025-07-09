my_book = Book.objects.get(id=1)
my_book_title = my_book.title
my_book_author = my_book.author
my_book_pub_year = my_book.publication_year

the command Book.objects.get(id=1) retrieves the intance of the first book in the database and assigns specific attributes to variables listed beneath it 