#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    x = int(input("Введите целое число: "))
    if x > 0:
        positive()
    elif x < 0:
        negative()
    else:
        print('x = 0')

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

if __name__ == '__main__':
    test()
