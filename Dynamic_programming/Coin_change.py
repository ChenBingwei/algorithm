#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回-1。

你可以认为每种硬币的数量是无限的。
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

"""
from common import utils


# 暴力解法
@utils.print_time
def func1(coins, amount):
    def dp(n):
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        # 求最小值，所以初始化为正无穷
        res = float('inf')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        return res if res != float('inf') else -1

    return dp(amount)


# 采用备忘录
@utils.print_time
def func2(coins, amount):
    memo = {}

    def dp(n):
        if n in memo:
            return memo[n]
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('inf')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)

        memo[n] = res if res != float('inf') else -1
        return memo[n]

    return dp(amount)


# 降低空间复杂度
@utils.print_time
def func3(coins, amount):
    def dp(n):
        # base case
        dp_list = [n + 1] * (n + 1)
        dp_list[0] = 0
        for i in range(0, n + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp_list[i] = min(dp_list[i], dp_list[i - coin] + 1)

        return dp_list[n] if dp_list[n] != n + 1 else -1

    return dp(amount)


if __name__ == '__main__':
    func1(coins=[1, 2, 5], amount=11)
    func2(coins=[1, 2, 5], amount=11)
    func3(coins=[1, 2, 5], amount=11)

# func: func1
# result: 3
# spent time:0.4880 ms
# ***************
# func: func2
# result: 3
# spent time:0.0310 ms
# ***************
# func: func3
# result: 3
# spent time:0.0231 ms
# ***************
