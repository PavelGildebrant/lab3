# Файл: models.py

class Group:
    """
    Класс (шаблон) для сущности "Группа".
    """
    def __init__(self, group_name, year, direction):
        # Атрибуты (данные) из овалов
        self.name = group_name      # 'название группы'
        self.year = year          # 'год поступления'
        self.direction = direction  # 'направления'

    # --- Методы ---

    def get_info(self):
        """
        Метод 1: Показывает информацию о группе.
        """
        return f"Группа: {self.name} (Напр: {self.direction}, Год: {self.year})"

#
# (Конец класса Group)