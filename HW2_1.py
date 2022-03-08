'''
1) Перегрузить оператор сложения.
Использовать метод __add__(). Он вызывается, когда объекты фигурируют с левой стороны.

Правосторонний метод перегрузки сложения - __radd__().

Возвращать метод __add__() может что угодно.
'''


class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

    def __str__(self):
        s = str(self.length) + ' ' + str(self.width) + ' ' + str(self.height)
        return s
    def __add__(self, other):
        return Table(self.length + other.length, self.width + other.width, self.height + other.height)

    def __radd__(self, other):
        return Table(self.length + other.length, self.width + other.width, self.height + other.height)


class DeskTable(Table):
    def square(self):
        return self.width * self.length


t1 = Table(1.5, 1.8, 0.75)
t2 = DeskTable(0.8, 0.6, 0.7)
t3 = t1 + t2
print(t3)