# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), 
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# 
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.
# 
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, structure):
        self.structure = structure

    def __str__(self):
        result_str = ""
        for row in self.structure:
            result_str += "|"
            for column in row:
                result_str += f"\t{column}"
            result_str += " |\n"        
        return result_str

    def __add__(self, other):
        if len(self.structure) == len(other.structure):
            return Matrix(
                [[col + other.structure[index][item_index]
                    for item_index, col in enumerate(row)] 
                        for index, row in enumerate(self.structure)]
            )
        else:
            print("Матрицы имеют разные размерности")
            return


stuff1 = Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

stuff2 = Matrix([[9, 8, 7],
                 [6, 5, 4],
                 [3, 2, 1]])

print(stuff1 + stuff2)