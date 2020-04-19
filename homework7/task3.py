# 3. Реализовать программу работы с органическими клетками. 
# Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), 
# вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
# умножение и обычное (не целочисленное) деление клеток, соответственно. 
# 
# В методе деления должно осуществляться округление значения до целого числа.
# 
# Сложение. Объединение двух клеток. 
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки. 
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух. 
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух. 
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), 
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n 
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, 
# то в последний ряд записываются все оставшиеся.
#
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
# Тогда метод make_order() вернет строку: **\n\n.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
# Тогда метод make_order() вернет строку: **\n\n***.

class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > 0 and other.quantity > 0 and self.quantity != other.quantity:
            return Cell(abs(self.quantity - other.quantity))
        else:
            print("Невозможно выполнить вычитание, количество клеток одинаково")
            return None

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if self.quantity == 0 or other.quantity == 0:
            print("Деление на ноль запрещено")
            return

        if self.quantity > other.quantity and other.quantity != 0:
            return Cell(self.quantity // other.quantity)
        else:
            self.quantity < other.quantity and self.quantity != 0
            return Cell(other.quantity // self.quantity)
    
    def make_order(self, quantity):
        rows = self.quantity // quantity
        tail = self.quantity % quantity
        result = ""
        for i in range(0, rows):
            result += "*" * quantity + "\n"

        result += tail * "*"

        return result

cell1 = Cell(101)
cell2 = Cell(10)

print((cell1 + cell2).quantity)
print((cell1 - cell2).quantity)
print((cell1 * cell2).quantity)
print((cell1 / cell2).quantity)
print(cell1.make_order(23))