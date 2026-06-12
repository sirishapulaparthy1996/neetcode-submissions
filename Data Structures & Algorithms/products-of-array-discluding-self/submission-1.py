class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        s = []
        for i in range(len(nums)):
            s.append(pre)
            pre *= nums[i]
        for j in range(len(nums)- 1, -1, -1):
            s[j] *= post
            post *= nums[j]

        return s

        
