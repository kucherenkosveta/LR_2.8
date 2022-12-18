#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

def cylinder():
    r = float(input('Введите радиус: '))
    h = float(input('Введите высоту: '))
    def circle():
        scircle = math.pi * r * r
        return scircle

    choice = input("1 - S боковой поверхности, 2 - S цилиндра: ")
    if choice == '1':
        print(2 * math.pi * r * h)
    elif choice == '2':
        print(2 * circle() + 2 * math.pi * r * h)
    else:
        print("Недопустимое значение!", file=sys.stderr)

if __name__ == '__main__':
    cylinder()