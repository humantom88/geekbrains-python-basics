# -*- coding:utf-8 -*-

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

if __name__ == "__main__" :
    arguments = sys.argv
    arguments.pop(0)

    if arguments[0] == "help" or arguments[0] == "--help" or arguments[0] == "-h":
        print("""
            Скрипт выполняет расчет зарплаты сотрудника.
            Параметры вводятся через пробел в следующем порядке:
            
            1. выработка в часах
            2. ставка в час
            3. премия

            Example:
            
            python 40 200 10000
            """)
    elif len(arguments) < 3:
        print('Вы ввели недостаточно параметров')
    else:
        try:
            workout_in_hours = int(arguments[0])
            hour_cost = int(arguments[1])
            award = int(arguments[2])

            salary = workout_in_hours * hour_cost + award

            print(f'Зарплата сотрудника: {salary}')
        except ValueError:
            print("В одном из параметров введено не число")