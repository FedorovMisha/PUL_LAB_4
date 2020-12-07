import math


# 27
def reversed_value(value):
    n = value
    n2 = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        n2 = n2 * 10
        n2 = n2 + digit

    return n2


# 25
def value_to_list(value):
    result = []
    for i in str(value):
        result.append(int(i))
    return result


# 8
def is_exists(a, b, c):
    return ((b + c - a) > 0) and ((a + c - b) > 0) and ((a + b - c) > 0)


def get_len(x1, y1, x2, y2):
    return math.sqrt(math.pow((y1 - y2), 2) + math.pow((x1 - x2), 2))


def get_square(a, b, c):
    return 0.25 * (math.sqrt((a + b + c) * (b + c - a) * (a + c - b) * (a + b - c)))


def task8():
    print("Введите координаты A:\n")
    xa, ya = int(input()), int(input())
    print("Введите координаты B:\n")
    xb, yb = int(input()), int(input())
    print("Введите координаты C:\n")
    xc, yc = int(input()), int(input())
    ab = get_len(xa, ya, xb, yb)
    bc = get_len(xb, yb, xc, yc)
    ca = get_len(xc, yc, xa, ya)
    if is_exists(ab, bc, ca):
        print("Площадь = ", get_square(ab, bc, ca))
    else:
        print("Треугольника не существует")


def get_min_divider_odd(value):
    for i in range(3, value):
        if value % i == 0 and i % 2 > 0:
            return i
    return -1


print("Задание 1: ")
print(reversed_value(54321))
print("Задание 2: ")
print(value_to_list(54321))
print("Задание 3: ")
task8()
print("Задание 4: ")
print(get_min_divider_odd(int(input())))
