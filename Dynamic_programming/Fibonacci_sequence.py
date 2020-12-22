#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。
该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。
"""
from common import utils


# func1: 暴力递归
@utils.print_time
def func1(num):
    def fib(n):
        if n in [1, 2]:
            return 1
        return fib(n - 1) + fib(n - 2)

    return fib(num)


# func2: 通过list备忘录来减少重复计算
@utils.print_time
def func2(num):
    def fib(n):
        if n < 1:
            return 0
        new_list = [0] * (n + 1)
        return fib_helper(new_list, n)

    def fib_helper(new_list, n):
        if n in [1, 2]:
            return 1
        if new_list[n] != 0:
            return new_list[n]
        new_list[n] = fib_helper(new_list, n - 1) + fib_helper(new_list, n - 2)
        return new_list[n]

    return fib(num)


# func3: 通过dict备忘录类减少重复计算
@utils.print_time
def func3(num):
    def fib(n):
        if n < 1:
            return 0
        init_dict = {}
        return fib_helper(init_dict, n)

    def fib_helper(init_dict, n):
        if n in [1, 2]:
            return 1
        if n in init_dict:
            return init_dict[n]
        init_dict[n] = fib_helper(init_dict, n - 1) + fib_helper(init_dict, n - 2)
        return init_dict[n]

    return fib(num)


# func4: 字典迭代解法
@utils.print_time
def func4(num):
    def fib(n):
        fib_dict = {
            1: 1,
            2: 1,
        }
        for i in range(3, n + 1):
            fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]
        return fib_dict[n]

    return fib(num)


# func5: 进一步优化空间复杂度
@utils.print_time
def func5(num):
    def fib(n):
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1
        prev = 1
        curr = 1
        for i in range(3, n + 1):
            next_value = prev + curr
            prev = curr
            curr = next_value
        return curr

    return fib(num)


if __name__ == '__main__':
    func1(15)
    func2(15)
    func3(15)
    func4(15)
    func5(15)

# func: func1
# result: 610
# spent time:0.2413 ms
# ***************
# func: func2
# result: 610
# spent time:0.0193 ms
# ***************
# func: func3
# result: 610
# spent time:0.0157 ms
# ***************
# func: func4
# result: 610
# spent time:0.0129 ms
# ***************
# func: func5
# result: 610
# spent time:0.0088 ms
# ***************
