class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = [1]*(len(nums))
        temp1 = 1
        for i in range(len(nums)):
            s[i]=temp1
            temp1*=nums[i]
        temp2 = 1
        for j in range(len(nums)-1,-1,-1):
            s[j]*=temp2
            temp2*=nums[j]
        return s
        
            

        