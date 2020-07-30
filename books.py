import json 

class BookDatabase:

    def __init__(self, filename, settings_file):
        self.database = {}
        self.settings ={}
        self.filename = filename
        self.settings_file = settings_file
    
    def get_database(self):
        return self.database

    def save(self):
        with open(self.filename, "w") as fptr:
            json.dump(self.database, fptr)

    def load(self):
        with open(self.filename, "r") as fptr:
            self.database = json.load(fptr)

    def load_settings(self):
        with open(self.settings_file, "r") as fptr:
            self.settings = json.load(fptr)

    def add_book(self, book_id, book):
        self.database[book_id] = book

    def get_by_isbn(self, isbn):
        return self.database.get(isbn)