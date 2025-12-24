# Файл: university_project/models/teacher.py

class Teacher:
    """
    Класс (шаблон) для сущности "Преподаватель".
    """
    def __init__(self, fio, degree, position):
        # Атрибуты (данные) из овалов
        self.fio = fio          # 'фио преподавателя'
        self.degree = degree    # 'ученая степень'
        self.position = position  # 'должность'

    # --- Методы ---

    def get_info(self):
        """
        Метод 1: Показывает информацию о преподавателе.
        """

        return f"{self.position}, {self.degree} {self.fio}"