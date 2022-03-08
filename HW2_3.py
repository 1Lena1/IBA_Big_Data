'''
Свойствам diametr и high объекта 
можно выполнять присваивание за пределами класса. 
Однако при этом "за кулисами" происходит пересчет площади,

Свойству area нельзя присваивать за пределами класса.
Можно только получать его значение.

Подсказка: вспомните про метод __setattr__(),
упомянутый в уроке про инкапсуляцию.'''
from math import pi

class Cylinder:
    def __init__(self, di, hi):
        self.diameter = di
        self.high = hi

    def __setattr__(self, attr, value):
        if (attr == 'diameter' or attr == 'high' ):
            self.__dict__[attr] = value
        else:
            raise AttributeError

    @staticmethod
    def make_area(di, hi):
        circle = pi * di ** 2 / 4
        side = pi * di * hi
        return round(circle * 2 + side, 2)
   
    def get_area(self):
        return self.make_area(self.diameter, self.high)

a = Cylinder(1, 2)
a.diameter = 10
print(a.get_area())

print(a.__dict__)
