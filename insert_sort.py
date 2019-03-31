#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
插入排序
"""
def insert_sort(alist):
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, n):
        # i代表内层循环起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i-1], alist[i] = alist[i], alist[i-1]
                i -= 1
            else:
                break