#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是[2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为O(n2) 。
进阶: 你能将算法的时间复杂度降低到O(nlogn) 吗?
"""
from time import time


def print_time(func):
    def wrappers(*args, **kwargs):
        start = time()
        print('func: {}'.format(func.__name__))
        print('result: {}'.format(func(*args, **kwargs)))
        end = time()
        print("spent time:%.4f" % ((end - start) * 1000))
        print("***************")

    return wrappers


# 动态规划解法
@print_time
def func1(num_list):
    def length_of_LIS(nums):
        dp_list = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp_list[i] = max(dp_list[i], dp_list[j] + 1)
        return max(dp_list)

    return length_of_LIS(num_list)

# 二分查找解法（来源于patience sorting纸牌游戏）
@print_time
def func2(num_list):
    def length_of_LIS(nums):
        pass
    return length_of_LIS(num_list)


if __name__ == '__main__':
    func1([10, 9, 2, 5, 3, 7, 101, 18])
