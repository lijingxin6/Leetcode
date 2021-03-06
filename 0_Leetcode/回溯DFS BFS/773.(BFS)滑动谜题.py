# -*- coding:utf-8 -*-
"""
author: lijingxin
Created on 12:51 PM 2/7/21
### [773\. 滑动谜题](https://leetcode-cn.com/problems/sliding-puzzle/)

Difficulty: **困难**


在一个 2 x 3 的板上（`board`）有 5 块砖瓦，用数字 `1~5` 来表示, 以及一块空缺用`0`来表示.

一次移动定义为选择`0`与一个相邻的数字（上下左右）进行交换.

最终当板`board`的结果是`[[1,2,3],[4,5,0]]`谜板被解开。

给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

**示例：**

```
输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成
```

```
输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板
```

```
输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]
```

```
输入：board = [[3,2,4],[1,5,0]]
输出：14
```

**提示：**

*   `board`是一个如上所述的 2 x 3 的数组.
*   `board[i][j]`是一个`[0, 1, 2, 3, 4, 5]`的排列.
 alt + shift + enter
"""
import collections
import json
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbor = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        m, n = 2, 3
        start = ""
        target = "123450"
        step = 0

        # 将2x3的数组转换成字符串
        for i in range(m):
            for j in range(n):
                start += chr(board[i][j] + ord('0'))

        # BFS
        visited = []
        queue = collections.deque([start])
        while queue:
            sz = len(queue)
            for _ in range(sz):
                cur = queue.popleft()

                # 判断是否达到目标局面
                if cur == target:
                    return step
                i = 0
                while (cur[i] != '0'):  # 找到数字 0 的索引
                    i += 1
                for adj in neighbor[i]:  # 数字 0 相邻位置的数字
                    new_board = list(cur)
                    new_board[adj], new_board[i] = new_board[i], new_board[adj]  # 将数字 0 和相邻的数字交换位置
                    new_board = "".join(new_board)
                    if (new_board not in visited):
                        queue.append(new_board)
                        visited.append(new_board)
            step += 1
        return -1

def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            board = stringToInt2dArray(line)

            ret = Solution().slidingPuzzle(board)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()