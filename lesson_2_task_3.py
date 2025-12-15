import math

def square(x):
    area = x ** 2
    print('Площадь квадрата=',area)
    return math.ceil(area)

side = 13.8
area = square(side)
print(f'Площидь квадрата с стороной {side} равна {area}')