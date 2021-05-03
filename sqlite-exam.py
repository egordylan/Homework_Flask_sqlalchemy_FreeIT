#импорт sqlite
import sqlite3

# подключаемся к базе данных коллекции книг
conn = sqlite3.connect('books-collection.db')

# создаем объект cursor, для работы с базой данных
c = conn.cursor()

# делаем запрос, который создает таблицу books с идентификатором и именем
c.execute('''
          CREATE TABLE books
          (id INTEGER PRIMARY KEY ASC,
	     name varchar(250) NOT NULL)
          ''' )

# выполняет запрос, который вставляет значения в таблицу
c.execute("INSERT INTO books VALUES(1, 'Чистый Python')")

# сохраняем работу
conn.commit()

# закрываем соединение
conn.close()
