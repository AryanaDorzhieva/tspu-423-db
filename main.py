import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id - INT(11) NOT NULL AUTO_INCREMENT
Фамилия - VARCHAR(60) NOT NULL
Имя - VARCHAR(30) NOT NULL
Отчество - VARCHAR(30)
Дата рождения - DATE NOT NULL
Email - VARCHAR(50) NOT NULL
Телефон - CHAR(20)
Форма обучения - ENUM("очная", "заочная", "очно-заочная") NOT NULL
Статус - TINYINT(1) NOT NULL DEFAULT = 1
Пароль - VARCHAR(32) NOT NULL
ID_факультета - INT(11) NOT NULL
ID_группы - INT(11) NOT NULL

)
''')

# Создаем таблицу Faculties
cursor.execute('''
CREATE TABLE IF NOT EXISTS Faculty (
id - INT(11) NOT NULL AUTO_INCREMENT
Название - VARCHAR(100) NOT NULL


)
''')

# Создаем таблицу Groups
cursor.execute('''
CREATE TABLE IF NOT EXISTS Groups (
id - INT(11) NOT NULL AUTO_INCREMENT
Название - VARCHAR(100) NOT NULL
ID_факультета - INT(11) NOT NULL

)
''')
# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
