#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import time


def PrintTime(func):
    def wrappers(*args, **kwargs):
        start = time()
        print('func: {}'.format(func.__name__))
        print('result: {}'.format(func(*args, **kwargs)))
        end = time()
        print("spent time:%.4f ms" % ((end - start) * 1000))
        print("***************")

    return wrappers


# fun1: 暴力递归
@PrintTime
def fun1(num):
    def fib(n):
        if n in [1, 2]:
            return 1
        return fib(n - 1) + fib(n - 2)

    return fib(num)


# fun2: 通过list备忘录来减少重复计算
@PrintTime
def fun2(num):
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


# fun3: 通过dict备忘录类减少重复计算
@PrintTime
def fun3(num):
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


# fun4: 字典迭代解法
@PrintTime
def fun4(num):
    def fib(n):
        fib_dict = {
            1: 1,
            2: 1,
        }
        for i in range(3, n + 1):
            fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]
        return fib_dict[n]

    return fib(num)


# fun5: 进一步优化空间复杂度
@PrintTime
def fun5(num):
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
    fun1(15)
    fun2(15)
    fun3(15)
    fun4(15)
    fun5(15)

# func: fun1
# result: 610
# spent time:0.2413 ms
# ***************
# func: fun2
# result: 610
# spent time:0.0193 ms
# ***************
# func: fun3
# result: 610
# spent time:0.0157 ms
# ***************
# func: fun4
# result: 610
# spent time:0.0129 ms
# ***************
# func: fun5
# result: 610
# spent time:0.0088 ms
# ***************
