#!/usr/bin/env python
# -*- coding:utf-8 -*-
def isVaild(self, s):
    """
    判断字符串左右括号是否匹配：用堆栈的方式
    :param self:
    :param s:
    :return:
    """
    stack = []
    paren_map = {')':'(',']':'[','}':'{'}
    for c in s:
        if c not in paren_map:
            stack.append()
        elif not stack or paren_map[c] != stack.pop():
            return False
    return not stack
