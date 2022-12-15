"""
4) Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен
показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40
(WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите
результат.
"""


class Car:
    """
    Класс машин
    """
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def to_go(self):
        """
        Метод отображения движения машины
        :return: строка состояния машины
        """
        return f'Машина {self.name} поехала'

    def stop(self):
        """
        Метод отображения остановки машины
        :return: строка состояния машины
        """
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        """
        Метод отображения поворота машины
        :return: строка состояния машины
        """
        return f'Машина {self.name} повернула на{direction}'

    def show_speed(self):
        """
        Метод отображения поворота машины
        :return: строка состояния машины
        """
        return f'Машина {self.name} едет со скоростью {self.speed} км/ч'

    def show_status(self):
        """Метод показывает, работает ли машина в полиции"""
        if self.is_police:
            return f'Машина {self.name} полицейская'
        return f'Машина {self.name} не полицейская'


class TownCar(Car):
    """
    Класс Городская машина
    """
    def __init__(self, *args):
        speed, color, name, is_police = args
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'У городской машины {self.name} превышена скорость: ' \
                   f'{self.speed} км/ч > 60 км/ч'
        return f'Городская машина {self.name} едет со скоростью {self.speed}' \
               f' км/ч'


class SportCar(Car):
    """
    Класс Спортивная машина
    """
    def __init__(self, *args):
        speed, color, name, is_police = args
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    """
    Класс Рабочая машина
    """
    def __init__(self, *args):
        speed, color, name, is_police = args
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'У рабочей машины {self.name} превышена скорость: ' \
                   f'{self.speed} км/ч > 40 км/ч'
        return f'Рабочая машина {self.name} едет со скоростью {self.speed}' \
               f' км/ч'


class PoliceCar(Car):
    """
    Класс Полицейская машина
    """
    def __init__(self, *args):
        speed, color, name, is_police = args
        super().__init__(speed, color, name, is_police)


toyota_ist = TownCar(55, 'красная', 'toyota ist', False)
print(toyota_ist.name)
print(toyota_ist.speed)
print(toyota_ist.color)
print(toyota_ist.is_police)
print(toyota_ist.to_go())
print(toyota_ist.stop())
print(toyota_ist.turn('лево'))
print(toyota_ist.turn('право'))
print(toyota_ist.show_speed())
print(toyota_ist.show_status())
print('')

toyota_LC_Prado = TownCar(100, 'черная', 'toyota Land Cruiser Prado', False)
print(toyota_LC_Prado.name)
print(toyota_LC_Prado.speed)
print(toyota_LC_Prado.color)
print(toyota_LC_Prado.is_police)
print(toyota_LC_Prado.to_go())
print(toyota_LC_Prado.stop())
print(toyota_LC_Prado.turn('лево'))
print(toyota_LC_Prado.turn('право'))
print(toyota_LC_Prado.show_speed())
print(toyota_LC_Prado.show_status())
print('')

toyota_supra = SportCar(120, 'желтая', 'toyota supra', False)
print(toyota_supra.name)
print(toyota_supra.speed)
print(toyota_supra.color)
print(toyota_supra.is_police)
print(toyota_supra.to_go())
print(toyota_supra.stop())
print(toyota_supra.turn('лево'))
print(toyota_supra.turn('право'))
print(toyota_supra.show_speed())
print(toyota_supra.show_status())
print('')

toyota_hilux = WorkCar(41, 'серая', 'toyota hilux', False)
print(toyota_hilux.name)
print(toyota_hilux.speed)
print(toyota_hilux.color)
print(toyota_hilux.is_police)
print(toyota_hilux.to_go())
print(toyota_hilux.stop())
print(toyota_hilux.turn('лево'))
print(toyota_hilux.turn('право'))
print(toyota_hilux.show_speed())
print(toyota_hilux.show_status())
print('')

ford_mustang = PoliceCar(130, 'сине-белая', 'ford mustang', True)
print(ford_mustang.name)
print(ford_mustang.speed)
print(ford_mustang.color)
print(ford_mustang.is_police)
print(ford_mustang.to_go())
print(ford_mustang.stop())
print(ford_mustang.turn('лево'))
print(ford_mustang.turn('право'))
print(ford_mustang.show_speed())
print(ford_mustang.show_status())
print('')
