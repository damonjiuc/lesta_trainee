from collections import deque

class rbuffer:

    def __init__(self, size):
        self.__data = deque()
        self.__size = size
        self.__count = 0

    def isEmpty(self):
        """ Возвращает True, если очередь буфера пуста """
        return self.__count == 0

    def isFull(self):
        """ Возвращает True, если очередь буфера заполнена """
        return self.__count == self.__size

    def push(self, data):
        """ Добавляет значение элемента в начало очереди,
            если очередь заполнена выбрасывает исключение
        """
        if self.isFull():
            raise Exception('Буфер заполнен')

        self.__data.append(data)

        self.__count += 1
    
    def pop(self):
        """ Убирает последний элемент буфера, возвращает его значение.
            В случае если буфер пуст выбрасывает исключение
        """
        if self.isEmpty():
            raise Exception('Буфер пуст')
        self.__count -= 1

        return self.__data.popleft()

    def info(self):
        """ Возвращает информацию о занятости буфера в виде строки {количество элементов}/{размер} """
        return f'{self.__count}/{self.__size}'

    def show(self):
        """ Возвращает список из элементов буфера """
        return f'{self.__data}'[6:-1]

    def clear(self):
        """ Сбрасывает буфер """
        self.__data.clear()