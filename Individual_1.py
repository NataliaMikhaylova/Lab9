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

    def set_sides(self, a, b, c):
        """
        Установка сторон
        :param a: сторона a
        :param b: сторона b
        :param c: сторона c
        :return:
        """
        self.side_a = a
        self.side_b = b
        self.side_c = c
        self._semi_perimeter = self.semi_perimeter()  # вычисляем полупериметр зарание, так как везде используем

    def set_angles(self, a, b, c):
        """
        Установка углов
        :param a: угол a
        :param b: угол b
        :param c: угол c
        :return:
        """
        self.angle_a = a
        self.angle_b = b
        self.angle_c = c

    def read(self):
        """
        Считывание исходных данных
        :return:
        """
        sides = list(map(int, input('Введите стороны треугольника: ').split()))
        self.set_sides(*sides)
        # В иделале нужно проверять что сумма углов равна 180
        angles = list(map(int, input('Введите углы треугольника: ').split()))
        self.set_angles(*angles)

    def perimeter(self):
        """
        Расчет периметра
        :return:
        """
        return self.side_a + self.side_b + self.side_c

    def semi_perimeter(self):
        """
        Расчет полуперимтера
        :return:
        """
        return self.perimeter() / 2

    def square(self):
        """
        Расчет площади по формуле Герона
        :return:
        """
        return (self._semi_perimeter
                * (self._semi_perimeter - self.side_a)
                * (self._semi_perimeter - self.side_b)
                * (self._semi_perimeter - self.side_c)
                ) ** 0.5

    def height(self, side_name):
        """
        Вычисление высоты опущенную на сторону side_name
        :param side_name: сторона (a, b, c)
        :return:
        """
        numerator = 2 * (self.square())
        denominator = 1
        if side_name == 'a':
            denominator = self.side_a
        if side_name == 'b':
            denominator = self.side_b
        if side_name == 'c':
            denominator = self.side_c
        return numerator / denominator

    def is_real(self):
        """
        Проверка существования треугольника
        :return:
        """
        return self.side_a + self.side_b > self.side_c \
            and self.side_a + self.side_c > self.side_b \
            and self.side_b + self.side_c > self.side_a


    def is_equilateral(self):
        """
        Определяем равносторонний ли треугольник
        :return:
        """
        return self.side_a == self.side_b == self.side_c

    def is_isosceles(self):
        """
        Определяем равнобедренный ли треугольник
        :return:
        """
        return self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c

    def is_rectangular(self):
        """
        Определяем по теореме Пифагора прямоугольный ли треугольник
        :return:
        """
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
