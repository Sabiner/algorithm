# coding: utf-8

__author__ = 'sabiner'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def declare_linked_list(array):
    """
    Declare linked list.
    :param array:
    :return:
    """
    if not array:
        return ListNode(None)

    linked = ListNode(array[0])
    linked_tmp = linked
    for i in array[1:]:
        linked_tmp.next = ListNode(i)
        linked_tmp = linked_tmp.next

    return linked
