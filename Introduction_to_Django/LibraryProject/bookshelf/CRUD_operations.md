# CRUD operations


## Create
command: 
```python 
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
#Expected Output:
#<Book: 1949 by George Orwell (1949)>
```

## Retrieve
command :

```python

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
#Expected Output:
#('1984', 'George Orwell', 1949)
```

## Update
command:

```python

book.title = "Nineteen Eighty-Four"
book.title()
#Expected Output:
#'Nineteen Eighty-Four'
```

## Delete
command:

```python

book.delete()
Book.objects.all()
#Expected Output:
#<QuerySet []>
```