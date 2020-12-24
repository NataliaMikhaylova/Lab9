#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triangle для представления треугольника. Поля данных должны включать
# углы и стороны. Требуется реализовать операции: получения и изменения полей данных,
# вычисления площади, вычисления периметра, вычисления высот, а также определения
# вида треугольника (равносторонний, равнобедренный или прямоугольный).

import math

class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self.angle_a = 0
        self.angle_b = 0
        self.angle_c = 0
        self._semi_perimeter = 0
        self._semi_perimeter = self.semi_perimeter()
        self.calc_angles()

    # Установка сторон
    def set_sides(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self._semi_perimeter = self.semi_perimeter()  # вычисляем полупериметр зарание, так как везде используем

    # Расчет углов треугольника
    def calc_angles(self):
        self.angle_b = math.degrees(math.acos((self.side_a ** 2 + self.side_c ** 2 - self.side_b ** 2)
                                              / (2 * self.side_a * self.side_c)))

        self.angle_c = math.degrees(math.acos((self.side_a ** 2 + self.side_b ** 2 - self.side_c ** 2)
                                                 / (2 * self.side_a * self.side_b)))

        self.angle_a = math.degrees(math.acos((self.side_b ** 2 + self.side_c ** 2 - self.side_a ** 2)
                                                 / (2 * self.side_b * self.side_c)))

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

    # Вычисление высоты опущенную на сторону side_name
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

    # Определяем равносторонний ли треугольник
    def is_equilateral(self):
        return self.side_a == self.side_b == self.side_c

    # Определяем равнобедренный ли треугольник
    def is_isosceles(self):
        return self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c

    # Определяем по теореме Пифагора прямоугольный ли треугольник
    def is_rectangular(self):
        # Сначала нужно найти гиппотинузу, она является большей стороной
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

    # Определяем прямоугольный ли треугольник по углам
    def is_rectangular2(self):
        return self.angle_a == 90 or self.angle_b == 90 or self.angle_c == 90

    # Определяем равносторонний ли треугольник по углам
    def is_equilateral2(self):
        return self.angle_a == self.angle_b == self.angle_c == 60

    def print_heights(self):
        name = ('a', 'b', 'c')
        for h in name:
            print('Высота опущенная на сторону {0}: {1:.3f}'.format(h, self.height(h)))

    def print_angle(self):
        print('alpha={0:.3f}, beta={1:.3f}, gamma={2:.3f}'.format(self.angle_a,
                                                                  self.angle_b,
                                                                  self.angle_c))

    def print_type(self):
        if self.is_equilateral2():
            print('Треугольник равносторонний')
            return
        if self.is_isosceles():
            print('Треугольник равнобедренный')
            return
        if self.is_rectangular2():
            print('Треугольник прямоуголный')
            return
        print('Треугольник разносторонний')


if __name__ == '__main__':
    sides = list(map(int, input('Введите стороны треугольника: ').split()))
    triangle = Triangle(*sides)
    if not triangle.is_real():
        print('Треугольник с заданными сторонами не существует')
        exit(0)
    print(triangle.square())
    triangle.print_angle()
    triangle.print_heights()
    triangle.print_type()
