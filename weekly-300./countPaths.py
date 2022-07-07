class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = {}
        visited = set()
        ans = 0
        MOD = 1000000007
        def dfs(node):
            if node in dp:
                return dp[node]
            visited.add(node)
            ans = 1
            i, j = node
            for next in [(i+1,j), (i-1, j), (i,j-1),(i,j+1)]:
                u,v = next
                if u < 0 or v < 0 or u >= m or v >= n or grid[u][v] <= grid[i][j]:
                    continue
                if next not in visited:
                    ans += dfs(next)
                else:
                    ans += dp[next]
            dp[node] = ans
            return ans
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    dfs((i,j))
                ans += dp[i,j]
            

        return ans % MOD
