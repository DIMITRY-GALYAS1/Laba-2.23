#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
С использованием многопоточности для заданного значения найти сумму
ряда с точностью члена ряда по абсолютному значению 1e-07 и
произвести сравнение полученной суммы с контрольным значением
функции для двух бесконечных рядов.
"""

import math
from threading import Thread

ABSOLUTE_VALUE = 1e-07


def compare_result(a, b):
    res = a - b
    print(f"Результат {res}")


def control_value():
    answer = 1 / (1 - 0.7)
    return answer


def row_1():
    s = 0
    n = 0
    x = 0.7
    previous = 0
    actual = math.pow(x, n)
    s += actual
    n += 1
    while abs(actual - previous) > ABSOLUTE_VALUE:
        previous = actual
        actual = math.pow(x, n)
        n += 1
        s += actual
    return s


def row_2():
    s = 0
    n = 0
    x = 1.2
    previous = 0
    actual = math.pow(-1, n) * (math.pow(x, n) / (math.pow(2, n + 1)))
    s += actual
    n += 1
    while abs(actual - previous) > ABSOLUTE_VALUE:
        previous = actual
        actual = math.pow(-1, n) * (math.pow(x, n) / (math.pow(2, n + 1)))
        n += 1
        s += actual
    return s


if __name__ == '__main__':
    r1 = Thread(target=compare_result(row_1(), control_value()))
    r1.start()
    r2 = Thread(target=compare_result(row_2(), control_value()))
    r2.start()
    r1.join()
    r2.join()
