# -*- coding:utf-8 -*-

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

phrase = [print(f'{index + 1}. {word[:10]}') for index, word in enumerate(input('Введите слова, разделенные пробелами: ').split())]

# P.S.: Очень хотелось сделать через генератор :-)