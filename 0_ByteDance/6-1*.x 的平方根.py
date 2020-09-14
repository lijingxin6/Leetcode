# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 9:54 PM 9/13/20
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans
    def mySqrt2(self, x: int) -> :
        if x == 0: return 0
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if (mid == x // mid):
                return mid
            if (mid < x // mid):
                left += 1
            else:
                right -= 1
        return right

def main():
    import sys
    import io
    def readlines():
        with open('stdin.txt') as f:
            for line in f:
                yield line.strip(('\n'))

    lines = readlines()
    while True:
        try:
            line = next(lines)
            x = int(line);

            ret = Solution().mySqrt(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()