* База данных

** Сущность пользователь

Поле - тип данных
```
id - INT(11) * AUTO_INCREMENT
Фамилия - VARCHAR(60) *
Имя - VARCHAR(30) *
Отчество - VARCHAR(30)
Дата рождения - DATE *
Email - VARCHAR(50) *
Телефон - CHAR(20)
Форма обучения - ENUM("очная", "заочная", "очно-заочная") *
Статус - TINYINT(1) * DEFAULT = 1
Пароль - VARCHAR(32) *
ID_факультета - INT(11) *
ID_группы - INT(11) *
```




```
** Сущнсоть Факультет

id - INT(11) * AUTO_INCREMENT
Название - VARCHAR(100) *
```



```
** Сущнсоть Группа

id - INT(11) * AUTO_INCREMENT
Название - VARCHAR(100) *
ID_факультета - INT(11) *
```





``` python
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS faculties (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL                       
    )''')

connection.commit()
connection.close()
```