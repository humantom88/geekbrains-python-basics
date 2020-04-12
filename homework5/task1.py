# 1. Создать программно файл в текстовом формате, 
# записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.

print('Введите текст: ')

with open('task1.txt', 'w') as f:
    is_input_over = False
    while not is_input_over:
        user_string = input()
        if len(user_string) == 0:
            is_input_over = True
        f.write(user_string + '\n')