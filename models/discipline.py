# Файл: university_project/models/discipline.py

class Discipline:
    """
    Класс (шаблон) для сущности "Дисциплина".
    """
    def __init__(self, name, hours, semester):
        # Атрибуты (данные) из овалов
        self.name = name          # 'название дисциплины'
        self.hours = hours        # 'количество часов'
        self.semester = semester  # 'семестр'

    # --- Методы ---

    def get_info(self):
        """
        Метод 1: Показывает информацию о дисциплине.
        """
        return f"Дисциплина: {self.name} (Семестр: {self.semester}, {self.hours} ч.)"