#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
栈的存储容器可以是链表，也可以是顺序表，在这里用list来保存
"""
class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加新的元素在栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()
    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        return None

    def is_empty(self):
        """判断栈是否为空"""
        return not self.__list

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push('1')
    s.push('2')
    s.push('3')
    s.push('4')
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())