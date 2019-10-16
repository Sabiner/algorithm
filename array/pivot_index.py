# coding: utf-8

__author__ = 'sabiner'


class Solution(object):
    """
    Leetcode - 724
    """
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0

        totalSum = sum(nums)
        startSum = 0
        for i in range(len(nums)):
            if startSum * 2 + nums[i] == totalSum:
                return i
            startSum += nums[i]
        return -1
