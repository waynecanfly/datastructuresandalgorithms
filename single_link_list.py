# -*- coding: utf-8 -*-
"""
python中变量的本质：
=右边的相当于去使用，所以首先要找到右边的变量所指向的是什么，=代表将右边变量位置赋值给左边，

链表和顺序表的比较：顺序表在存取元素时可以一次定位（时间复杂度O（1）），但是顺序表的存储空间必须是连续的，存储数据大的时候，顺序表达不到要求。
                  链表对分散的存储空间可以达到充分的利用，但是同时开销也变大了（需要保存下一个元素的链接区），并且在存取是不能一次定位。
                  插入时顺序表和链表的时间复杂度都是O(n)，但是不同，链表主要花费在遍历链表过程，顺序表花费在腾空间。
"""

class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None



class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node
    def is_empty(self):
        """链表是否为空"""
        return self.__head == None
    def length(self):
        """获取链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count 计数器
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个列表"""
        cur = self.__head
        while cur != None:
            print(cur.elem,end=' ')
            cur = cur.next


    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

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
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是不是头结点
                # 头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
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




if __name__ == '__main__':
    ll = SingleLinkList()
    print(ll.is_empty())
    ll.add(9)
    ll.travel()
    print(ll.length())

    # ll.append(1)
    # print(ll.is_empty())
    # print(ll.length())
    #
    # ll.append(2)
    # ll.append(3)
    # ll.add(8)
    # ll.append(4)
    # ll.append(5)
    # ll.append(6)
    # ll.append(7)
    #
    # ll.travel()