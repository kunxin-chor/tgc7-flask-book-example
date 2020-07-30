from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from books import BookDatabase
from ProcessCreateBook import ProcessCreateBook
import os


load_dotenv()

app = Flask(__name__)

# create an object based on the class BookDatabase
bookDB = BookDatabase("books.json", "settings.json")
bookDB.load()
bookDB.load_settings()

createBookProcess = ProcessCreateBook(bookDB)


@app.route('/')
def all_books():
    return render_template('view_all.template.html', books=bookDB.get_database())

@app.route('/create_book')
def create_book():
    return render_template('create_book.template.html', settings=bookDB.settings)


@app.route('/create_book', methods=["POST"])
def process_book():
    title = request.form.get('title')
    isbn = request.form.get('ISBN')
    genre = request.form.get('genre')
    category = request.form.get('category')

    # middle-man, this is known as a SERVICE
    createBookProcess.create_book(title, isbn, genre, category)
    return "book saved"



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)