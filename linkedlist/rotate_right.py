# coding: utf-8

from declare_linked_list import declare_linked_list


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    @staticmethod
    def rotate_right(head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        old_tail = head
        list_len = 1
        while old_tail and old_tail.next:
            list_len += 1
            old_tail = old_tail.next

        old_tail.next = head

        new_tail = head
        for i in range(list_len - k % list_len - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
