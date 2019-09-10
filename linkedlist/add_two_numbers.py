# coding: utf-8

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
__author__ = 'sabiner'

from declare_linked_list import ListNode, declare_linked_list


class Solution(object):

    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(None)
        dummy.next = curr
        tmp = 0

        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            isum = num1 + num2 + tmp
            curr.next = ListNode(isum % 10)

            curr = curr.next
            tmp = isum / 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if tmp:
            curr.next = ListNode(tmp)

        return dummy.next


if __name__ == '__main__':
    l1 = declare_linked_list([2, 4, 3])
    l2 = declare_linked_list([5, 6, 4])
    result = Solution.add_two_numbers(l1, l2)
    print result
