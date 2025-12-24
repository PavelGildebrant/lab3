import sqlite3  # Подключаем библиотеку

# 1. Создаем соединение с базой в памяти (RAM)
conn = sqlite3.connect(':memory:')

# 2. Создаем курсор (инструмент для выполнения команд)
cursor = conn.cursor()

print("База данных подключена!")


# 3. Пишем SQL-запрос для создания таблицы группы
sql_create_group = '''
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT,
    year INTEGER,
    direction TEXT
)
'''

# 4. Просим курсор выполнить этот запрос
cursor.execute(sql_create_group)
print("Таблица groups создана.")


# --- 5. Подготовка списка данных ---
# Мы создаем список, в котором лежат данные для 5 групп.
# Формат: (Название, Год, Направление)
groups_data = [
    ('ИБ-1', 2024, 'Инф. Без.'),
    ('ИБ-2', 2024, 'Инф. Без.'),
    ('ПИ-1', 2023, 'Прикл. Инф.'),
    ('ОЗИ-1', 2022, 'ОЗИ'),
    ('ГК-1', 2021, 'Геодезия')
]
# --- 6. Вставка данных (INSERT) ---
# executemany — спец. команда: "Возьми весь список и вставь каждую строку"
# Знаки вопроса (?, ?, ?) — это места, куда подставятся данные из списка
cursor.executemany("INSERT INTO groups (group_name, year, direction) VALUES (?, ?, ?)", groups_data)
# --- 7. Сохранение изменений (COMMIT) ---
# Обязательный шаг! Без него данные не запишутся в базу.
conn.commit()
print("Группы успешно добавлены.")


# --- 8. Проверка (SELECT) ---

print("\n--- Проверяем содержимое таблицы groups: ---")
cursor.execute("SELECT * FROM groups")
rows = cursor.fetchall()

for row in rows:
    print(row)

# --- 9. Создание таблицы Студентов  ---

cursor.execute("DROP TABLE IF EXISTS students")

sql_create_students = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio TEXT,
    birth_date TEXT,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
)
'''
cursor.execute(sql_create_students)
print("Таблица students создана .")

students_data = [
    ('Иванов И.И.', '20.01.2005', 1),
    ('Петров П.П.', '15.05.2004', 1),
    ('Сидорова А.В.', '03.11.2005', 3),
    ('Козлов Д.С.', '10.08.2004', 3),
    ('Новикова Е.А.', '25.12.2005', 4)
]
cursor.executemany("INSERT INTO students (fio, birth_date, group_id) VALUES (?, ?, ?)", students_data)
conn.commit()
print("Студенты добавлены.")
# --- 13. Таблица Преподавателей ---
cursor.execute("DROP TABLE IF EXISTS teachers") # На всякий случай удаляем старую
sql_create_teachers = '''
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio TEXT,
    degree TEXT,
    position TEXT
)
'''
cursor.execute(sql_create_teachers)

teachers_data = [
    ('Петров В.С.', 'Кандидат технических наук', 'Доцент'),
    ('Максимова О.И.', 'Кандидат физ.-мат. наук', 'Доцент'),
    ('Синицын А.В.', 'Доктор технических наук', 'Профессор'),
    ('Белов Ю.А.', 'Без степени', 'Ст. преподаватель'),
    ('Кузнецова М.Д.', 'Кандидат экономических наук', 'Ассистент')
]
cursor.executemany("INSERT INTO teachers (fio, degree, position) VALUES (?, ?, ?)", teachers_data)
conn.commit()
print("Таблица teachers создана и заполнена.")


# --- 14. Таблица Дисциплин ---
cursor.execute("DROP TABLE IF EXISTS disciplines")
sql_create_disciplines = '''
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    hours INTEGER,
    semester INTEGER
)
'''
cursor.execute(sql_create_disciplines)

disciplines_data = [
    ('Базы данных', 144, 4),
    ('Криптография', 108, 4),
    ('Python', 144, 3),
    ('Физкультура', 72, 1),
    ('Математика', 180, 1)
]
cursor.executemany("INSERT INTO disciplines (name, hours, semester) VALUES (?, ?, ?)", disciplines_data)
conn.commit()
print("Таблица disciplines создана и заполнена.")


# --- 15. Таблица Оценивания  ---
# Здесь мы ссылаемся на ТРИ другие таблицы сразу
cursor.execute("DROP TABLE IF EXISTS gradings")
sql_create_gradings = '''
CREATE TABLE gradings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade TEXT,
    date TEXT,
    control_type TEXT,
    student_id INTEGER,
    teacher_id INTEGER,
    discipline_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id),
    FOREIGN KEY (discipline_id) REFERENCES disciplines(id)
)
'''
cursor.execute(sql_create_gradings)

# Данные: Оценка, Дата, Тип, ID Студента, ID Преподавателя, ID Дисциплины
gradings_data = [
    ('5', '01.06.2025', 'Экзамен', 1, 1, 1), # Студент 1 получил 5 у Преподавателя  1 по Дисциплине 1
    ('4', '30.05.2025', 'Экзамен', 2, 1, 1),
    ('Зачет', '25.05.2025', 'Зачет', 1, 2, 2),
    ('3', '15.01.2025', 'Экзамен', 3, 3, 3),
    ('Незачет', '18.12.2024', 'Зачет', 4, 4, 4)
]
cursor.executemany("INSERT INTO gradings (grade, date, control_type, student_id, teacher_id, discipline_id) VALUES (?, ?, ?, ?, ?, ?)", gradings_data)
conn.commit()
print("Таблица gradings создана и заполнена.")

# --- 16. ФИНАЛ: Задание на UPDATE и DELETE ---

print("\n--- Демонстрация UPDATE (Изменение) ---")
print("До изменения (Преподаватель id=4):")
cursor.execute("SELECT * FROM teachers WHERE id=4")
print(cursor.fetchone())

# Повышаем Белова (id=4) до Доцента
cursor.execute("UPDATE teachers SET position = 'Доцент' WHERE id = 4")
conn.commit()

print("После изменения:")
cursor.execute("SELECT * FROM teachers WHERE id=4")
print(cursor.fetchone())


print("\n--- Демонстрация DELETE (Удаление) ---")
# Удаляем оценки "Незачет"
cursor.execute("DELETE FROM gradings WHERE grade = 'Незачет'")
conn.commit()
print("Записи с оценкой 'Незачет' удалены.")

print("\n--- Итоговый список оценок: ---")
cursor.execute("SELECT * FROM gradings")
for row in cursor.fetchall():
    print(row)

print("\n" + "="*30)
print("   ФИНАЛЬНАЯ ПРОВЕРКА БАЗЫ   ")
print("="*30)

# 1. Проверяем Группы
print("\n--- 1. Таблица GROUPS (Группы) ---")
# id | Название | Год | Направление
cursor.execute("SELECT * FROM groups")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 2. Проверяем Студентов
print("\n--- 2. Таблица STUDENTS (Студенты) ---")
# id | ФИО | Дата рожд. | id_группы
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 3. Проверяем Преподавателей
print("\n--- 3. Таблица TEACHERS (Преподаватели) ---")
# id | ФИО | Степень | Должность
# внимание: Белов (id=4) должен быть "Доцентом"
cursor.execute("SELECT * FROM teachers")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 4. Проверяем Дисциплины
print("\n--- 4. Таблица DISCIPLINES (Дисциплины) ---")
# id | Название | Часы | Семестр
cursor.execute("SELECT * FROM disciplines")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 5. Проверяем Оценки
print("\n--- 5. Таблица GRADINGS (Оценивание) ---")
# id | Оценка | Дата | Тип | id_студ | id_преп | id_дисц
# внимание: тут НЕ должно быть оценки "Незачет"
cursor.execute("SELECT * FROM gradings")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n" + "="*30)
# Закрываем соединение
conn.close()
print("\nРабота завершена.")
