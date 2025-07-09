my_book = Book.objects.get(title="1984")
my_book.title = "Nineteen Eighty-Four"

just like before, I got the instance of the model by querying for a particular column the title column and gave it a new name