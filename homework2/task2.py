# -*- coding:utf-8 -*-

# 2. Для списка реализовать обмен значений соседних элементов, т.е. 
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

foo = input('Введите значения списка через пробел: ').split()
piece1 = foo[::2]
piece2 = foo[1::2]
result = []

for index, item in enumerate(piece2):
    result.append(item)
    result.append(piece1[index])
    
if len(foo) % 2 != 0:
    result.append(foo[-1])

print(result)