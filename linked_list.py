#!/usr/bin/env python
# -*- coding:utf-8 -*-

def reverseList(self, head):
    """
    反转链表:定义两个指针，分别指向当前节点cur，与当前节点的前驱结点prev，实现反转链表的思路： cur.next-->prev-->cur-->cur.next 要注意是的是当前节点与前后节点都要保持连接防止断链
    """
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev
def swapPairs(self, head):
    """
    链表交换相邻元素
    :param self:
    :param head:
    :return:
    """
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next

def hasCycle(self, head):
    """
    判断链表中是否存在环：1、硬判断，在指定时间段内，判断指针是否指向None
    2、将循环的节点保存在set中,每次判断新节点是否在set中
    3、快慢指针法：如果链表中存在环，那么快慢指针必定会相遇
    :param self:
    :param head:
    :return:
    """
    fast= slow= head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False