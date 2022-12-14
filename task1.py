"""
1) Создать класс TrafficLight (светофор) и определить у него один атрибут color
(цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках
метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго
(желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение
между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный
метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его
нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep

# Первый вариант
class Trafficlight:
    """
    Класс для описания светофоров
    """
    __color = ''
    def running(self):
        """
        Симуляция работы светофора
        :return: Вывод в консоль состояния
        """
        self.__color = 'Красный'
        print(f'Светофор переключился на: {self.__color}')
        sleep(7)
        self.__color = 'Желтый'
        print(f'Светофор переключился на: {self.__color}')
        sleep(2)
        self.__color = 'Зеленый'
        print(f'Светофор переключился на: {self.__color}')
        sleep(10)
        self.__color = ''


my_trafficlight = Trafficlight()
my_trafficlight.running()


# Второй вариант
class Trafficlight1:
    """
    Класс для описания светофоров
    """
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running(self):
        """
        Симуляция работы светофора
        :return: Вывод в консоль состояния
        """
        i = 0
        while i < len(self.__color):
            if i == 0:
                print(f'Загорается: {self.__color[i]}')
                sleep(7)
            elif i == 1:
                print(f'Загорается: {self.__color[i]}')
                sleep(2)
            elif i == 2:
                print(f'Загорается: {self.__color[i]}')
                sleep(10)
            i += 1


my_trafficlight_v2 = Trafficlight1()
my_trafficlight_v2.running()
