#!/usr/bin/env python
# -*- coding:utf-8 -*-

def quick_sort(alist):
    """快速排序"""
    n = len(alist)
    mid_value = alist[0]
    low = 0
    high = n-1
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        low += 1

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        high -= 1