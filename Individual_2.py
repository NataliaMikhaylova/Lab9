#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triad (тройка чисел); определить методы изменения полей и вычисления
# cуммы чисел. Определить производный класс Triangle с полями-сторонами. Определить
# методы вычисления углов и площади треугольника.

import math


class Triad:
    def __init__(self):
        self._a = 0
        self._b = 0
        self._c = 0

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def set_a(self, value):
        self._a = value

    def set_b(self, value):
        self._b = value

    def set_c(self, value):
        self._c = value

    # Считывание исходных данных
    def read(self):
        for i in range(1, 4):
            line = int(input('Введите число {0}: '.format(i)))
            if i == 1:
                self.set_a(value=line)
            if i == 2:
                self.set_b(value=line)
            if i == 3:
                self.set_c(value=line)

    def sum(self):
        return self._a + self._b + self._c


class Triangle(Triad):
    def __init__(self):
        super(Triangle, self).__init__()
        self.angles = Triad()

    # Расчет улов треугольника
    def calc_angles(self):
        self.angles.set_b(math.degrees(math.acos((self.get_a() ** 2 + self.get_c() ** 2 - self.get_b() ** 2)
                                       / (2 * self.get_a() * self.get_c())))
                          )
        self.angles.set_c(math.degrees(math.acos((self.get_a() ** 2 + self.get_b() ** 2 - self.get_c() ** 2)
                                       / (2 * self.get_a() * self.get_b())))
                          )
        self.angles.set_a(math.degrees(math.acos((self.get_b() ** 2 + self.get_c() ** 2 - self.get_a() ** 2)
                                       / (2 * self.get_b() * self.get_c())))
                          )

    # Расчет площади по двум сторонам и углу между ними
    def square(self):
        self.calc_angles()
        return (self.get_b()*self.get_c()*math.sin(math.radians(self.angles.get_a()))) / 2


if __name__ == '__main__':
    triangle = Triangle()
    triangle.read()
    triangle.calc_angles()
    print('alpha={0:.3f}, beta={1:.3f}, gamma={2:.3f}'.format(triangle.angles.get_a(),
                                                              triangle.angles.get_b(),
                                                              triangle.angles.get_c()))
    print('Сумма углов треугольника равна {0}'.format(triangle.angles.sum()))
    print('Площадь треугольника равна {0:.3f}'.format(triangle.square()))