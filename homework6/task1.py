# -*- coding:utf-8 -*-

# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут 
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный. 
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, 
# третьего (зеленый) — на ваше усмотрение. 
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить 
# соответствующее сообщение и завершать скрипт.

import time
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = 'RED'
        self.__durability = {
            'RED': 7,
            'YELLOW': 2,
            'GREEN': 5
        }
        self.__order = ['RED', 'YELLOW', 'GREEN', 'YELLOW']
    
    def running(self):
        for color in cycle(self.__order):
            self.__color = color
            print(self.__color)
            time.sleep(self.__durability[color])

traffic_light = TrafficLight()
traffic_light.running()