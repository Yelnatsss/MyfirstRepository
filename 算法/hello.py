from typing import List
from collections import deque
class Solution:
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    marked[i][j] = True
                    queue = deque()
                    queue.append((i,j))
                    while queue:
                        cur_x ,cur_y = queue.popleft()
                        # cur_x, cur_y = queue.popleft()
                        for direction in self.directions:
                            new_x = direction[0] + cur_x
                            new_y = direction[1] + cur_y
                            if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and grid[new_x][new_y] == '1':
                                marked[new_x][new_y] = True
                                queue.append((new_x,new_y))
        return count


if __name__ == "__main__":
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)
