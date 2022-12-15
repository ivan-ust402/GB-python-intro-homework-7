"""
2) Реализовать класс Road (дорога), в котором определить атрибуты: length
(длина), width (ширина). Значения данных атрибутов должны передаваться при
создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    """
    Класс для создания объектов дорог
    """
    single_asphalt_mass = 25
    height_road = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass_asphalt(self):
        """
        Метод расчета полной массы асфальта для требуемой длины и ширины
        дорожного полотна
        :return: строка результата
        """
        road_mass = round(self._width * self._length *
                          self.single_asphalt_mass * self.height_road / 1000)
        return f'Масса асфальта, для дороги\nдлиной - {self._length} ' \
               f'метров,\nшириной - {self._width} метров,\n' \
               f'высотой полотна - {self.height_road} сантиметров\n' \
               f'равна {road_mass} тонн'


m54_first_part = Road(5000, 20)
print(m54_first_part.calc_mass_asphalt())
