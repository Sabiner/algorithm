# coding: utf-8

__author__ = 'sabiner'

import unittest
from algorithm import declare_linked_list, removeElements


class TestRemoveElements(unittest.TestCase):

    def test_remove_elements(self):
        head = declare_linked_list([1, 2, 6, 3, 4, 5, 6])
        removeElements.remove_elements(head, 6)
        while head:
            assert head.val != 6
            head = head.next
