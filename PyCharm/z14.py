# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def get_input():
    return input('Введите число: ')

def test_input(x):
    if x.isnumeric():
        return True
    else:
        return False

def str_to_int(x):
    return int(x)

def print_int(x):
    print(x)

if __name__ == '__main__':
    a = get_input()
    if test_input(a):
        print(str_to_int(a))
    else:
        print("Введенно не целое число", file=sys.stderr)
