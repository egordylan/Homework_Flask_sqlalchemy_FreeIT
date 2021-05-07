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


# Уникальные значения жанров
#@app.route('/books/genres/', methods=['GET'])
#def uniqueGenre(genre):
#    unique_list = []  # Добавляем пустой список для уникальных значений
#    listOfGenre = session.query(Book).filter_by(genre=genre).all()
#
    # Смотрим все элементы editedBook = session.query(Book).filter_by(id=book_id).one()
#    for genre in listOfGenre:
#        # Проверка на существование элемента в листе уникальных
#        if genre not in listOfGenre:
#            unique_list.append(genre)
#        for genre in unique_list:
#            return genre
#    return render_template('genreBook.html', books=listOfGenre)
# SELECT authors, title FROM book GROUP BY genre ORDER BY genre;


# Добавляем группировку книг по жанрам
@app.route('/books/genre/', methods=['GET'])
def genreBook():
#    genreOfBook = session.query(Book).group_by(Book.genre).order_by(Book.genre).all()
    genreOfBook = session.query(Book).group_by(Book.genre).distinct(Book.genre).order_by(Book.genre).all()
#    for value in session.query(Book.genre).distinct():
#        unique_genres = []
#        if value not in unique_genres:
#            unique_genres.append(value)
#        elif value in unique_genres:
#            return # шоб я понимала и знала что тут должно быть. пойду побьюсь головой о стену
#        elif value is None:
#            return


    session.commit()
    return render_template('genreBook.html', books=genreOfBook)


if __name__ == '__main__':
    app.debug = True
    app.run(port=4996)

