#!/usr/bin/env python
# -*- coding:utf-8 -*-
class dequeue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []
    def add_front(self, item):
        """从队头加入一个item元素"""
        self.__list.insert(0, item)
    def add_rear(self, item):
        """从队尾加入一个item元素"""
        self.__list.append(item)
    def remove_front(self):
        """从队头删除元素"""
        self.__list.pop(0)
    def remove_rear(self):
        """从队尾删除元素"""
        self.__list.pop()
    def is_empty(self):
        """判断双端队列是否为空"""
        return not self.__list
    def size(self):
        """返回队列的大小"""
        return len(self.__list)