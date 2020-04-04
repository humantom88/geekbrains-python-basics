# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def summarize_max_couple(first, second, third):
    numbers = [first, second, third]
    first_max = max(numbers)
    numbers.remove(first_max)
    second_max = max(numbers)

    return first_max + second_max

try:
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    third = int(input('Введите третье число: '))
    result = summarize_max_couple(first, second, third)
    
    print(f'Сумма двух максимальных: {result}')
except ValueError:
    print('Введено неверное значение')  