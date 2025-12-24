# Файл: main.py
# ---  Создаем и проверяем все 5 классов ---
# 1. Импортируем ВСЕ 5 "моделей" из папки 'models'
from models.discipline import Discipline
from models.grading import Grading
from models.group import Group
from models.student import Student
from models.teacher import Teacher

# --- 2. Создание 5 экземпляров Групп ---
print("--- 1. Создание 5 экземпляров Групп ---")
g1 = Group(group_name="ИБ-1", year=2024, direction="Инф. Без.")
g2 = Group(group_name="ИБ-2", year=2024, direction="Инф. Без.")
g3 = Group(group_name="ПИ-1", year=2023, direction="Прикл. Инф.")
g4 = Group(group_name="ОЗИ-1", year=2022, direction="ОЗИ")
g5 = Group(group_name="ГК-1", year=2021, direction="Геодезия")
# --- Проверка методов Групп ---
print("\n--- Проверка методов Групп ---")
print(f"Объект g1: {g1.get_info()}")
print(f"Объект g2: {g2.get_info()}")
print(f"Объект g3: {g3.get_info()}")
print(f"Объект g4: {g4.get_info()}")
print(f"Объект g5: {g5.get_info()}")


# --- 3. Создание 5 экземпляров Студентов ---
print("\n--- 2. Создание 5 экземпляров Студентов ---")
s1 = Student(fio="Иванов Иван Иванович", birth_date="20.01.2005", group_object=g1)
s2 = Student(fio="Петров Петр Петрович", birth_date="15.05.2004", group_object=g1)
s3 = Student(fio="Сидорова Анна Викторовна", birth_date="03.11.2005", group_object=g3)
s4 = Student(fio="Козлов Дмитрий Сергеевич", birth_date="10.08.2004", group_object=g3)
s5 = Student(fio="Новикова Елена Андреевна", birth_date="25.12.2005", group_object=g4)

# --- Проверка методов Студентов ---
print("\n--- Проверка методов Студентов ---")
print(f"Объект s1: {s1.get_info()}")
print(f"Объект s2: {s2.get_info()}")
print(f"Объект s3: {s3.get_info()}")
print(f"Объект s4: {s4.get_info()}")
print(f"Объект s5: {s5.get_info()}")


# --- 4. Создание 5 экземпляров Преподавателей ---
print("\n--- 3. Создание 5 экземпляров Преподавателей ---")
t1 = Teacher(fio="Петров Василий Сергеевич", degree="Кандидат технических наук", position="Доцент")
t2 = Teacher(fio="Максимова Ольга Ивановна", degree="Кандидат физико-математических наук", position="Доцент")
t3 = Teacher(fio="Синицын Андрей Викторович", degree="Доктор технических наук", position="Профессор")
t4 = Teacher(fio="Белов Юрий Алексеевич", degree="Без ученой степени", position="Старший преподаватель")
t5 = Teacher(fio="Кузнецова Мария Дмитриевна", degree="Кандидат экономических наук", position="Ассистент")

# --- Проверка методов Преподавателей ---
print("\n--- Проверка методов Преподавателей ---")
print(f"Объект t1: {t1.get_info()}")
print(f"Объект t2: {t2.get_info()}")
print(f"Объект t3: {t3.get_info()}")
print(f"Объект t4: {t4.get_info()}")
print(f"Объект t5: {t5.get_info()}")


# --- 5. Создание 5 экземпляров Дисциплин ---
print("\n--- 4. Создание 5 экземпляров Дисциплин ---")
d1 = Discipline(name="Базы данных", hours=144, semester=4)
d2 = Discipline(name="Основы криптографии", hours=108, semester=4)
d3 = Discipline(name="Программирование на Python", hours=144, semester=3)
d4 = Discipline(name="Физическая культура", hours=72, semester=1)
d5 = Discipline(name="Высшая математика", hours=180, semester=1)

# --- Проверка методов Дисциплин ---
print("\n--- Проверка методов Дисциплин ---")
print(f"Объект d1: {d1.get_info()}")
print(f"Объект d2: {d2.get_info()}")
print(f"Объект d3: {d3.get_info()}")
print(f"Объект d4: {d4.get_info()}")
print(f"Объект d5: {d5.get_info()}")


# --- 6. Создание 5 экземпляров Оценивания ---
print("\n--- 5. Создание 5 экземпляров Оценивания ---")
# ВНИМАНИЕ: Мы передаем объекты s, t, d в конструктор!
gr1 = Grading(grade=5, date="01.06.2025", control_type="Экзамен", student_obj=s1, teacher_obj=t1, discipline_obj=d1)
gr2 = Grading(grade=4, date="30.05.2025", control_type="Экзамен", student_obj=s2, teacher_obj=t1, discipline_obj=d1)
gr3 = Grading(grade="Зачет", date="25.05.2025", control_type="Зачет", student_obj=s1, teacher_obj=t2, discipline_obj=d2)
gr4 = Grading(grade=3, date="15.01.2025", control_type="Экзамен", student_obj=s3, teacher_obj=t3, discipline_obj=d3)
gr5 = Grading(grade="Незачет", date="18.12.2024", control_type="Зачет", student_obj=s4, teacher_obj=t4, discipline_obj=d4)

# --- Проверка методов Оценивания ---
print("\n--- Проверка методов Оценивания (get_full_record) ---")
print(f"Запись 1: {gr1.get_full_record()}")
print(f"Запись 2: {gr2.get_full_record()}")
print(f"Запись 3: {gr3.get_full_record()}")
print(f"Запись 4: {gr4.get_full_record()}")
print(f"Запись 5: {gr5.get_full_record()}")

print("\n--- Программный модуль завершен ---")