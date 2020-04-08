# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

number = int(input("Введите начало отсчета (целое число): "))

for i in count(number):
    print(i)

cycle_list = ['In', 'The', 'End', 'It', 'Doesn\'t', 'Even', 'Matter']
for i in cycle(cycle_list):
    print(i)