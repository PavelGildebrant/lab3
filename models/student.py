class Student:
    """
    Класс (шаблон) для сущности "Студент".
    """
    def __init__(self, fio, birth_date, group_object):
        # Атрибуты (данные) из овалов
        self.fio = fio                  # 'фио студента'
        self.birth_date = birth_date    # 'дата рождения'

        # ВАЖНО: Реализация связи 1:*
        # Этот атрибут хранит ОБЪЕКТ Группы, к которой
        # принадлежит студент
        self.group = group_object

    # --- Методы ---

    def get_info(self):
        """
        Метод 1: Показывает информацию о студенте
        Использует 'self.group.name' для получения
        названия группы из связанного объекта.
        """
        return f"Студент: {self.fio} (Группа: {self.group.name}, ДР: {self.birth_date})"