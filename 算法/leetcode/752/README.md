# 752. 打开转盘锁

## 题目描述和难度

- 题目描述   
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 题目 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

- 示例 1:

**输入:**  `deadends = ["0201","0101","0102","1212","2002"], target = "0202"`

**输出:**  `6`

- **解释：**  可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。

- **提示**

死亡列表 deadends 的长度范围为 [1, 500]。
目标数字 target 不会在 deadends 之中。
每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生

**题目难度：**  中等

**中文地址**  [打开转盘锁](https://leetcode-cn.com/problems/open-the-lock/)

## 思路分析

关键求解：借助队列用广度优先算法（BFS），建立搜索树，求最短路径

- `from queue import Queue`对比`from collections import deque` 优先使用速度更快的前者

-  `in`操作在优先将`list`转`set`

## 参考答案
### 参考代码1
```python
from collections import deque# 优先考虑 collections 而不是queue中队列
from typing import List
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #总体思路BFS算法，借助队列这种数据结构。求起始点到目标点最短路径
        deadends =set(deadends)#当要做查找操作时要将队列转换成set否则严重超时，set中查找时间复杂度O（1）
        queue =deque()
        if "0000" in deadends:
            return -1

        #队列第一个参数存储要尝试的点，第二参数存储当前步数
        #从0000开始尝试，入列等待处理
        queue.append(("0000",0))
        while queue:
            #每次旋转会在4个节点中选一个（i记录），
            #此节点只有+1，或-1两种旋转情况（j记录）。
            #因此每次旋转有8中可能性
            node, step = queue.popleft()
            for i in range(4):
                for j in (-1,1):
                    # 中间为变化部分，两边不变。
                    cur = node[:i]+str((int(node[i])+j)%10)+node[i+1:]
                    if  cur == target:#尝试后相等则step +1输出
                        return step + 1
                    else:#不相等
                        if not cur in deadends:#若在不在死亡队列，将此节点压入队列等待下一次尝试
                            queue.append((cur,step+1))
                            deadends.add(cur) #去重
        return -1
```



