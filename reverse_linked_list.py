#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
反转链表:定义两个指针，分别指向当前节点cur，与当前节点的前驱结点prev，实现反转链表的思路： cur.next-->prev-->cur-->cur.next 要注意是的是当前节点与前后节点都要保持连接防止断链
"""
def reverseList(self, head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev