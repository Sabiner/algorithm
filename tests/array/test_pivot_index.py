# coding: utf-8

import unittest
from algorithm import pivotIndex

__author__ = 'sabiner'


class TestPivotIndex(unittest.TestCase):

    def test_pivot_index(self):
        nums = [1, 7, 3, 6, 5, 6]
        pivot = pivotIndex().pivotIndex(nums)
        assert pivot == 3
