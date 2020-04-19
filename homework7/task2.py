# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
# К типам одежды в этом проекте относятся пальто и костюм. 
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. 
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы 
# для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Cloth(ABC): 
    def __init__(self, name):
        self.name = name
    
    @property
    @abstractmethod
    def material_amount(self):
        pass

class Coat(Cloth):
    def __init__(self, size):
        super().__init__("Пальто")
        self.size = size
    
    @property
    def material_amount(self):
        return self.size / 6.5 + 0.5

class Suit(Cloth):
    def __init__(self, height):
        super().__init__("Костюм")
        self.height = height

    @property
    def material_amount(self):
        return self.height * 2 + 0.3

suit = Suit(180)
coat = Coat(52)

print(suit.material_amount)
print(coat.material_amount)