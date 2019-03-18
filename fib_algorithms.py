#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
斐波那契数列算法
"""


def fib(n):
    if n < 1:
        return -1
    if (1 == n) or (2 == n):
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    a = fib(6)
    print(a)