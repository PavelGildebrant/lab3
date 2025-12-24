# Файл: university_project/models/grading.py

class Grading:
    """
    Класс (шаблон) для сущности "Оценивание".
    Реализует связи с Student, Teacher, Discipline.
    """

    def __init__(self, grade, date, control_type, student_obj, teacher_obj, discipline_obj):
        # Атрибуты (данные) из овалов
        self.grade = grade  # 'бал оценивания' (напр. 5 или "Зачет")
        self.date = date  # 'дата оценивания' (напр. "01.06.2025")
        self.control_type = control_type  # 'форма контроля' (напр. "Экзамен")

        # Атрибуты для реализации связей
        self.student = student_obj  # Объект класса Student
        self.teacher = teacher_obj  # Объект класса Teacher
        self.discipline = discipline_obj  # Объект класса Discipline

    # --- Метод 1 ---
    def get_full_record(self):
        """Метод 1: Показывает полную запись об оценивании, используя информацию из связанных объектов."""
        student_info = self.student.fio
        discipline_name = self.discipline.name
        teacher_info = self.teacher.get_info()  # Используем метод get_info() преподавателя
        return (f"Студент: {student_info} получил '{self.grade}' "
                f"по '{discipline_name}' от '{teacher_info}'. "
                f"({self.control_type}, {self.date})")
    # --- МЕТОД 2 (НОВЫЙ) ---
    def is_passed(self):
        """Метод 2: Проверяет, сдана ли дисциплина (True/False)."""
        # "Зачет" - это строка, поэтому проверяем ее отдельно
        if isinstance(self.grade, str) and self.grade.lower() == "зачет":
            return True
        # Оценки (5, 4, 3) - это числа
        if isinstance(self.grade, int) and self.grade >= 3:
            return True
        # Все остальное ("Незачет", 2) - это False
        return False