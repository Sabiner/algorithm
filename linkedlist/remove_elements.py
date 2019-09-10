# coding: utf-8

"""
删除链表中等于给定值 val 的所有节点。
原地操作

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
__author__ = 'sabiner'

from declare_linked_list import ListNode, declare_linked_list


class Solution(object):

    @staticmethod
    def remove_elements(head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head

        # 给链表一个哑节点指针
        tmp = ListNode(None)
        tmp.next = head
        head = tmp

        # 记住头节点
        dummy = head

        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next


if __name__ == '__main__':
    head = declare_linked_list([1, 2, 6, 3, 4, 5, 6])
    Solution.remove_elements(head, 6)
