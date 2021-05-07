import sys
# для настройки баз данных
from sqlalchemy import Column, PrimaryKeyConstraint, ForeignKey, Integer, String

# для определения таблицы и модели
from sqlalchemy.ext.declarative import declarative_base

# для создания отношений между таблицами
from sqlalchemy.orm import relationship

# для настроек
from sqlalchemy import create_engine

# создание экземпляра declarative_base
Base = declarative_base()


# мы создаем класс Book наследуя его из класса Base.
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250), nullable=True)

#class Genre(Book):
#    __tablename__ = 'genres'

#    id = Column(Integer, primary_key=True)
#    genre = Column(String(250), nullable=True)

    # Добавляем пустой список для уникальных значений
#    unique_list = []

    # Смотрим все элементы editedBook = session.query(Book).filter_by(id=book_id).one()
#    for item in genre:
        # Проверка на существование элемента в листе уникальных
        #if item not in Book:
        #    unique_list.append(item)
        #elif item in unique_list:
        #    pass
#        unique_list = sorted(list(set(Book)))

#def get_unique_numbers(numbers):
#    unique = []
#    for number in numbers:
#        if number not in unique:
#            unique.append(number)
#    return unique


#class Genre(Book):
#    __tablename__ = 'genres'

#    id = Column(Integer, primary_key=True)
#    genre = Column(String(250), nullable=True)

    # Добавляем пустой список для уникальных значений
#    unique_list = []

    # Смотрим все элементы editedBook = session.query(Book).filter_by(id=book_id).one()
#    for item in genre:
        # Проверка на существование элемента в листе уникальных
        #if item not in Book:
        #    unique_list.append(item)
        #elif item in unique_list:
        #    pass
#        unique_list = sorted(list(set(Book)))

#def get_unique_numbers(numbers):
#    unique = []
#    for number in numbers:
#        if number not in unique:
#            unique.append(number)
#    return unique

# создает экземпляр create_engine в конце файла
engine = create_engine('sqlite:///books-collection.db')

Base.metadata.create_all(engine)
