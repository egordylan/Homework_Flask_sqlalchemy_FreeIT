# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Book
from itertools import groupby


app = Flask(__name__)

# Подключаемся и создаем сессию базы данных
engine = create_engine('sqlite:///books-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# страница, которая будет отображать все книги в базе данных
# Эта функция работает в режиме чтения.
@app.route('/')
@app.route('/books')
def showBooks():
    books = session.query(Book).all()
    return render_template("books.html", books=books)


# Эта функция позволит создать новую книгу и сохранить ее в базе данных.
@app.route('/books/new/', methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        newBook = Book(title=request.form['name'], author=request.form['author'], genre=request.form['genre'])
        session.add(newBook)
        session.commit()
        return redirect(url_for('showBooks'))
    else:
        return render_template('newBook.html')


# Эта функция позволит нам обновить книги и сохранить их в базе данных.
@app.route("/books/<int:book_id>/edit/", methods=['GET', 'POST'])
def editBook(book_id):
    editedBook = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['name'] or request.form['author'] or request.form['genre']:
            editedBook.title = request.form['name']
            editedBook.author = request.form['author']
            editedBook.genre = request.form['genre']
            session.commit()
            return redirect(url_for('showBooks'))
    else:
        return render_template('editBook.html', book=editedBook)


# Эта функция для удаления книг
@app.route('/books/<int:book_id>/delete/', methods=['GET', 'POST'])
def deleteBook(book_id):
    bookToDelete = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        session.delete(bookToDelete)
        session.commit()
        return redirect(url_for('showBooks', book_id=book_id))
    else:
        return render_template('deleteBook.html', book=bookToDelete)


# Добавляем группировку книг по жанрам
@app.route('/books/genre/', methods=['GET'])
def genreBook(filed=None):
    genre_of_book = session.query(Book).all()
    dictionary = dict()
    for book in genre_of_book:  # Local variable 'book' value is not used
        book_list = []
        dictionary[book.genre] = book_list
    for book in genre_of_book:
        book_list = dictionary.get(book.genre)
        book_list.append(book)

#    for book in genre_of_book:
#        dictionary = {}
#        book_list = []
#        if dictionary.get(Book.genre) is None:
#            dictionary[Book.genre] = book_list
#        else:
#            dictionary.get(Book.genre).append(book)
#    session.commit()
    return render_template('genreBook.html', books=dictionary)  #books - переменная в виде именованных аргументов, которые вы хотите передать движку обработки шаблонов


if __name__ == '__main__':
    app.debug = True
    app.run(port=4996)

