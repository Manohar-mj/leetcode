class Solution:
    def minimumNumbers(self, nums: int, k: int) -> int:
        req=[]
        for i in range(nums+1):
            if str(i)[-1]==str(k):
                req.append(i)
        dp=[float("inf")]*(nums+1)
        dp[0]=0
        for i in range(1,nums+1):
            for j in req:
                if i-j>=0:
                    dp[i]=min(dp[i],dp[i-j]+1)
        if dp[nums]==float("inf"):
            return -1
        return dp[nums]
