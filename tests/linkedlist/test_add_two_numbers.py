# coding: utf-8

__author__ = 'sabiner'

import unittest
from algorithm import declare_linked_list, addTwoNumbers


class TestAddTwoNumbers(unittest.TestCase):

    def test_add_two_numbers(self):

        l1 = declare_linked_list([2, 4, 3])
        l2 = declare_linked_list([5, 6, 4])
        result = addTwoNumbers.add_two_numbers(l1, l2)

        assert result.val == 7
        assert result.next.val == 0
        assert result.next.next.val == 8

    def test_add_empty(self):

        l1 = declare_linked_list([1, 2])
        l2 = declare_linked_list([5, 6, 4])
        result = addTwoNumbers.add_two_numbers(l1, l2)

        assert result.val == 6
        assert result.next.val == 8
        assert result.next.next.val == 4
