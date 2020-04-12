# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from functools import reduce

with open('task5.txt', 'w') as f:
    f.write(" ".join([str(i) for i in range(1, 100, 2)]))

with open('task5.txt', 'r') as f:
    result = reduce(lambda acc, line: int(acc) + int(line), f.readline().split())
    print(result)
    
