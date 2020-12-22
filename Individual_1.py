#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triangle для представления треугольника. Поля данных должны включать
# углы и стороны. Требуется реализовать операции: получения и изменения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).

class Triangle:
    def __init__(self):
        self.side_a = 0
        self.side_b = 0
        self.side_c = 0
        self.angle_a = 0
        self.angle_b = 0
        self.angle_c = 0
        self._semi_perimeter = 0

    # Установка сторон
    def set_sides(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self._semi_perimeter = self.semi_perimeter()  # вычисляем полупериметр зарание, так как везде используем

    # Установка углов
    def set_angles(self, a, b, c):
        self.angle_a = a
        self.angle_b = b
        self.angle_c = c

    # Считывание исходных данных
    def read(self):
        sides = list(map(int, input('Введите стороны треугольника: ').split()))
        self.set_sides(*sides)
        # В иделале нужно проверять что сумма углов равна 180
        angles = list(map(int, input('Введите углы треугольника: ').split()))
        self.set_angles(*angles)

    # Расчет периметра
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    # Расчет полуперимтера
    def semi_perimeter(self):
        return self.perimeter() / 2

    # Расчет площади по формуле Герона
    def square(self):
        return (self._semi_perimeter
                * (self._semi_perimeter - self.side_a)
                * (self._semi_perimeter - self.side_b)
                * (self._semi_perimeter - self.side_c)
                ) ** 0.5

    # Вычисление высоты опущенную на сторону
    def height(self, side_name):
        numerator = 2 * (self.square())
        denominator = 1
        if side_name == 'a':
            denominator = self.side_a
        if side_name == 'b':
            denominator = self.side_b
        if side_name == 'c':
            denominator = self.side_c
        return numerator / denominator

    # Проверка существования треугольника
    def is_real(self):
        return self.side_a + self.side_b > self.side_c \
            and self.side_a + self.side_c > self.side_b \
            and self.side_b + self.side_c > self.side_a


    # Определяем вид треугольника
    def is_equilateral(self):
        return self.side_a == self.side_b == self.side_c

    def is_isosceles(self):
        return self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c

    def is_rectangular(self):
        # Сначала нужно найти гипотинузу, она является большей стороной
        if self.side_a > self.side_b:
            if self.side_a > self.side_c:
                return self.side_a ** 2 == self.side_b ** 2 + self.side_c ** 2
            else:
                return self.side_c ** 2 == self.side_b ** 2 + self.side_a ** 2
        else:
            if self.side_b > self.side_c:
                return self.side_b ** 2 == self.side_a ** 2 + self.side_c ** 2
            else:
                return self.side_c ** 2 == self.side_a ** 2 + self.side_b ** 2

    def print_heights(self):
        name = ('a', 'b', 'c')
        for h in name:
            print('Высота опущенная на сторону {0}: {1:.3f}'.format(h, self.height(h)))

    def print_type(self):
        if self.is_equilateral():
            print('Треугольник равносторонний')
            return
        if self.is_isosceles():
            print('Треугольник равнобедренный')
            return
        if self.is_rectangular():
            print('Треугольник прямоуголный')
            return
        print('Треугольник разносторонний')


if __name__ == '__main__':
    triangle = Triangle()
    triangle.read()
    if not triangle.is_real():
        print('Треугольник с заданными сторонами не существует')
        exit(0)
    print(triangle.square())
    triangle.print_heights()
    triangle.print_type()
