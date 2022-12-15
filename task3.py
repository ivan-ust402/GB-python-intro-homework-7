"""
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на
базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).
"""


class Worker:
    """
    Класс для создания объектов работник
    """
    def __init__(self, *args):
        name, surname, position, wage, bonus = args
        self.name = name
        self.surname = surname
        self. position = position
        self._income = {"wage": wage, "bonus": bonus}

    def go_work(self):
        """
        Метод для описания действия работника
        :return: строка описани действия
        """
        return f'{self.position} {self.name} {self.surname} усердно работает'

    def get_lunch(self):
        """
        Метод для описания действия работника
        :return: строка описани действия
        """
        return f'{self.position} {self.name} {self.surname} обедает'


class Position(Worker):
    """
    Класс наследующийся от базового класса Worker
    """
    def __init__(self, *args):
        name, surname, position, wage, bonus, age = args
        super().__init__(name, surname, position, wage, bonus)
        self.age = age

    def get_full_name(self):
        """
        Метод получения полного имени сотрудника
        :return: строка полного имени
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
        Метод получения информации о доходе сотрудника с учетом премии
        :return: число дохода
        """
        return self._income.get('wage') + self._income.get('bonus')


first_worker = Position('Игорь', 'Васильев', 'инженер', 35000, 5000, 35)
print(first_worker.get_full_name())
print(first_worker.get_total_income())
print(first_worker.name)
print(first_worker.surname)
print(first_worker.position)
print(first_worker.age)
print(first_worker.go_work())
print(first_worker.get_lunch())
# print(first_worker._income)
