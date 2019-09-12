# coding: utf-8

__author__ = 'sabiner'

import unittest
from algorithm import declare_linked_list, rotateRight


class TestRotateRight(unittest.TestCase):

    def test_rotate_right(self):
        array = [1, 2, 3, 4, 5]
        step = 2

        moved = step % len(array)
        array_result = array[-moved:] + array[:-moved]
        linked_list = declare_linked_list(array)
        result = rotateRight.rotate_right(linked_list, step)
        for i in array_result:
            assert result.val == i
            result = result.next

    def test_rotate_circle(self):
        array = [0, 1, 2]
        step = 4

        moved = step % len(array)
        array_result = array[-moved:] + array[:-moved]
        linked_list = declare_linked_list(array)
        result = rotateRight.rotate_right(linked_list, step)
        for i in array_result:
            assert result.val == i
            result = result.next
