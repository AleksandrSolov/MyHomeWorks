
#class Example:
#    def __new__(cls, *args, **kwargs):
 #       print(args)
#        print(kwargs)
 #       return object.__new__(cls)
#    def __init__(self, first, second, third):
#        print(first)
#        print(second)
 #       print(third)
#ex = Example('data', second=25, third=3.14)
#"""
#('data',)
#{'second': 25, 'third': 3.14}
#data
#25
#3.14
#"""
class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        #print(*cls.houses_history)
        return super().__new__(cls)
    
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
             return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
    def __it__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.__eq__(other) or self.__it__(other)
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)
    def __ne__(self, other):
        return  not self.__eq__(other)
    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return  self.__add__(value)

    def __del__(self):
        print(self.name, 'снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
"""
Вывод на консоль:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Эльбрус снесён, но он останется в истории
"""