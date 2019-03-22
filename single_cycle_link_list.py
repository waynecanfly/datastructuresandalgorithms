#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
class SingleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node
    def is_empty(self):
        """链表是否为空"""
        return self.__head == None
    def length(self):
        """获取链表长度"""
        # cur游标，用来移动遍历节点
        if self.is_empty():
            return 0
        cur = self.__head
        # count 计数器
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个列表"""
        if self.is_empty():
            return None
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem,end=' ')
            cur = cur.next
        # 退出循环,cur指向为结点,将尾结点打印出来
        print(cur.elem)


    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """
        在指定位置添加元素
        :param pos 从0开始
        """
        """定义游标pre指向前一节点"""
        if pos <= 0:
            self.add(item)
        elif pos >= (self.length()):
            self.append()
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos-1):
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除元素"""
        """定义两个游标，一个指向当前节点，另一个指向当前节点的前一个节点"""
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:
                    # 先判断此节点是不是头结点
                    # 头结点
                    #找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间结点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == item:
            if cur == self.__head:
                # 链表只有一个结点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        """判断节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.elem == item:
            return True
        return False
