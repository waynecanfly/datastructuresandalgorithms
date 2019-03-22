#!/usr/bin/env python
# -*- coding:utf-8 -*-
from single_link_list import SingleLinkList


class Node(object):
    def __init__(self, item):
        """结点"""
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(SingleLinkList):
    """双链表"""
    # def __init__(self, node=None):
    #     self.__head = node
    # def is_empty(self):
    #     """链表是否为空"""
    #     return self.__head == None
    # def length(self):
    #     """获取链表长度"""
    #     # cur游标，用来移动遍历节点
    #     cur = self.__head
    #     # count 计数器
    #     count = 0
    #     while cur != None:
    #         count += 1
    #         cur = cur.next
    #     return count
    #
    # def travel(self):
    #     """遍历整个列表"""
    #     cur = self.__head
    #     while cur != None:
    #         print(cur.elem,end=' ')
    #         cur = cur.next


    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素，尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

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
            cur = self.__head
            node = Node(item)
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 当循环退出后,cur指向pos位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def remove(self, item):
        """删除元素"""
        """定义两个游标，一个指向当前节点，另一个指向当前节点的前一个节点"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是不是头结点
                # 头结点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        #判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    cur.next,prev = cur.prev
                break
            else:
                cur = cur.next


    def search(self, item):
        """判断节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False