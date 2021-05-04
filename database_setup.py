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



# создает экземпляр create_engine в конце файла
engine = create_engine('sqlite:///books-collection.db')

Base.metadata.create_all(engine)
