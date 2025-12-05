import math

def area(r):
    '''
    Вычисляет площадь круга.
    
    Параметры:
        r (float): радиус круга
    
    Возвращаемое значение:
        float: площадь круга
    '''
    if r < 0 :
        raise ValueError("Стороны не могут быть отрицательными")
    return math.pi * r * r

def perimeter(r):
    '''
    Вычисляет длину окружности.
    
    Параметры:
        r (float): радиус круга
    
    Возвращаемое значение:
        float: длина окружности
    
    '''
    if r < 0 :
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * math.pi * r
