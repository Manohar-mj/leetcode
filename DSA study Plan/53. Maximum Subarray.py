def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        cursub=0
        for i in nums:
            if cursub<=0:
                cursub=0
            cursub+=i
            maxsub=max(maxsub,cursub)
        return maxsub
