class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        arr=set()
        for a,b in zip(nums,nums[1:]):
            if a+b in arr:
                return True
            arr.add(a+b)
        return False
