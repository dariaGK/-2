import math


def area(r):
    '''
        Назначение: Возвращает площадь круга

        Входные данные:

            r (float): радиус окружности

        Возвращаемое значение:

            cr_area (float): площадь круга с радиусом r

        Пример вызова:
            result = area(2)
            print(result)
            12,56
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Назначение: Возвращает длину окружности

        Входные данные:

            r (float): радиус окружности

        Возвращаемое значение:

            cr_perimeter (float): длина окружности с радиусом r

        Пример вызова:
            result = perimeter(2)
            print(result)
            12,56
    '''
    return 2 * math.pi * r

