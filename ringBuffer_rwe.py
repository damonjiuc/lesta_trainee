""" Циклический буфер, с задаваемой длиной, на основе списка
>>> x = rbuffer(3)
>>> x.info()
'0/3'
>>> x.show()
[]
>>> x.push(1)
>>> x.info()
'1/3'
>>> x.push(2)
>>> x.push(3)
>>> x.pick(7)
[1, 2, 3, 1, 2, 3, 1]
>>> x.push(4)
Traceback (most recent call last):
    ...
Exception: Буфер заполнен
>>> x.show()
[1, 2, 3]
>>> x.pop()
1
>>> x.show()
[2, 3]
>>> x.pick(5)
[2, 3, 2, 3, 2]
>>> x.pop()
2
>>> x.pop()
3
>>> x.pop()
Traceback (most recent call last):
    ...
Exception: Буфер пуст
"""

class rbuffer:
    
    def __init__(self, size:int):
        self.__elements = [0] * size
        self.__first = 0
        self.__last = 0
        self.__count = 0
        self.__size = size

    def push(self, element):
        """ Добавляет значение элемента в начало очереди,
            если очередь заполнена выбрасывает исключение
        """
        if self.__count == self.__size:
            raise Exception('Буфер заполнен')

        self.__elements[self.__first] = element

        self.__count += 1
        self.__first = self.next_index(self.__first)

    def pop(self):
        """ Убирает последний элемент буфера, возвращает его значение.
            В случае если буфер пуст выбрасывает исключение
        """
        if self.isEmpty():
            raise Exception('Буфер пуст')

        element = self.__elements[self.__last]

        self.__count -= 1
        self.__last = self.next_index(self.__last)
        return element

    def next_index(self, index):
        """ Увеличивает индекс элемента списка на 1, 
            если он равен длине списка - переходит в его начало
        """
        index += 1
        if index == self.__size:
            index = 0
        return index
    
    def info(self):
        """ Возвращает информацию о занятости буфера в виде строки {количество элементов}/{размер} """
        return f'{self.__count}/{self.__size}'

    def pick(self, number:int):
        """ Проходит по {number} элементов буфера от последнего элемента к первому,
            возвращает список пройденных элементов """
        if self.isEmpty():
            return []

        mass = []
        index = self.__last
        for _ in range(number):
            mass.append(self.__elements[index])
            index = self.next_index(index)
            if index == self.__first:
                index = self.__last                
        return mass

    def show(self):
        """ Возвращает список из элементов буфера """
        return self.pick(self.__count)

    def isEmpty(self):
        """ Возвращает True, если очередь буфера пуста """
        return self.__count == 0

    def isFull(self):
        """ Возвращает True, если очередь буфера заполнена """
        return self.__count == self.__size

    def clear(self):
        """ Сбрасывает буфер """
        self.__first = self.__last = self.__count = 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()