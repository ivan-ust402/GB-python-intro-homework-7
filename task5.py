"""
5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем
атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
“Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать
экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    """
    Класс канцелярская принадлежность
    """
    def __init__(self, title):
        self.title = title

    def draw(self):
        """
        Метод запуска отрисовки
        :return: строка сообщения о начале действия
        """
        return 'Запуск отрисовки'


class Pen(Stationery):
    """
    Класс ручка
    """
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """Ручка пишет чернилами"""
        return f'{self.title} - фирма производитель ручек. Ручка' \
               f' пишет чернилами. Это универсальный инструмент.'


class Pencil(Stationery):
    """
    Класс карандаш
    """
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """Карандаш чертит графитом"""
        return f'{self.title} - фирма производитель карандашей. Карандаш' \
               f'чертит графитом. Карандаш легко удаляется ластиком.'


class Handle(Stationery):
    """
    Класс маркер
    """
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        """Маркер пишет краской"""
        return f'{self.title} - фирма производитель маркеров. Маркер' \
               f'закрашивает краской. Маркер служит для выделения важных слов.'


pen = Pen('Erich Krause')
print(pen.title)
print(pen.draw())
print('')
pencil = Pencil('Нижний тагил')
print(pencil.title)
print(pencil.draw())
print('')
handle = Handle('Marker')
print(handle.title)
print(handle.draw())
print('')

feather_ink = Stationery('Перо и чернила')
print(feather_ink.title)
print(feather_ink.draw())
print('')
