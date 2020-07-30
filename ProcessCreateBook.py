class ProcessCreateBook:

    def __init__(self, database):
        self.database = database
    
    def create_book(self, title, isbn, genre, category):

        if self.database.get_by_isbn(isbn) is not None:
            return False # cannot add a book with duplicated ISBN

        book = {
            "isbn": isbn,
            "title": title,
            "genre": genre,
            "category": category
        }

        self.database.add_book(isbn, book)
        self.database.save()
        return True
