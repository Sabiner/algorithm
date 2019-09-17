# coding: utf-8

__author__ = 'sabiner'


class Node(object):

    def __init__(self, key, value, nex):
        self.key = key
        self.value = value
        self.nex = nex


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = 10000
        self.bucket = [Node(None, None, None) for _ in range(self.numbers)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        val = key % self.numbers
        head = self.bucket[val]
        while head.nex:
            if head.key == key:
                head.value = value
            head = head.nex

        if head.key == key:
            head.value = value
        else:
            head.nex = Node(key, value, None)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        val = key % self.numbers
        head = self.bucket[val]
        while head:
            if head.key == key:
                return head.value
            head = head.nex
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        val = key % self.numbers
        head = self.bucket[val]
        while head and head.nex:
            if head.nex.key == key:
                head.nex = head.nex.nex
            head = head.nex


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print obj.get(1)
print obj.get(3)
obj.put(2, 1)
print obj.get(2)
obj.remove(2)
print obj.get(2)
