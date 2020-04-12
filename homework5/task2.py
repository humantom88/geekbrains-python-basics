# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task2.txt', 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        print(f'{index + 1}: {len(line.split())}')