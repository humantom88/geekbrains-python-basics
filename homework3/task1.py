# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    try:
        print(f'Результат: {dividend / divider}')
    except:
        print('Делить на ноль нельзя')

try:
    users_dividend = int(input('Введите делимое: '))
    users_divisor = int(input('Введите делитель: '))
    division(users_dividend, users_divisor)
except ValueError:
    print('Введено неверное значение')    