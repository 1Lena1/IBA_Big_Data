'''
2) Разработать класс, который наследует функциональность типа str
 и содержит 2 новых метода:

метод is_repeatance (s), который принимает 1 аргумент s
и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым количеством повторов строки s.
Вернуть False, если s не является строкой.
Считать, что пустая строка не содержит повторов.

метод is_palindrom (), который возвращает True или False
в зависимости от того, является ли строка палиндромом.
Регистрами символов пренебрегать. Пустую строку считать палиндромом.
'''

class Super_str(str):
    def __init__(self, s):
        self.__Str = s

    def is_repeatance(self, s):
        if isinstance(self.__Str, str) and self.__Str != '':
            for i in range(len(self.__Str)+1):
                if i*s == self.__Str:
                    return True
        return False

    def is_palindrom(self):
        return self.__Str == self.__Str[::-1]


a = Super_str('qwewq')
print(a.is_repeatance('qw'))
print(a.is_palindrom())
