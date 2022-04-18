class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2,nums1)
        c=Counter(nums1)
        res=[]
        for i in nums2:
            if c[i] >0:
                res.append(i)
                c[i]-=1
        return res
