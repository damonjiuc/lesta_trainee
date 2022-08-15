# исходная функция
def isEven(value):
    """ Исходная функция """
    return value % 2 == 0

def isEvenBit(value):
    """ Определение четности побитовым оператором """
    return not value & 1
    
if __name__ == '__main__':
    from random import randrange
    from time import time

    A = [randrange(9999999999, 99999999999) for i in range(10000)]
    
    start = time()
    for number in A:
        isEven(number)
    end = time()
    print(f"Example: {end - start}s")

    start = time()
    for number in A:
        isEvenBit(number)
    end = time()
    print(f"Bit &  : {end - start}s")