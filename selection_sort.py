#!/usr/bin/env python
# -*- coding:utf-8 -*-
def selection_sort(alist):
    """
    选择排序
    最优时间复杂度O(n^2)
    最坏时间复杂度O(n^2)
    """
    n = len(alist)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1, n):
            if alist[i] < alist[min_index]:
                min_index = i
    alist[j], alist[min_index] = alist[min_index], alist[j]