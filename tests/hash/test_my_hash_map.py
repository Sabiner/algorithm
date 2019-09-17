# coding: utf-8

import unittest

__author__ = 'sabiner'
from algorithm import myHashMap


class TestHashMap(unittest.TestCase):

    def test_my_hash_map(self):
        obj = myHashMap()
        obj.put(1, 1)
        obj.put(2, 2)
        assert obj.get(1) == 1
        assert obj.get(3) == -1
        obj.put(2, 1)
        assert obj.get(2) == 1
        obj.remove(2)
        assert obj.get(2) == -1
