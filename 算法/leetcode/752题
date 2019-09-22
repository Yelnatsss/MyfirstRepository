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
solution =Solution()
print(solution.openLock(["0000"],"8888"))
