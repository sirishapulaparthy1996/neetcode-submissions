class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        nums = set(nums)
        for i in nums:
            longest = 1
            if i-1 not in nums:
                while i+longest in nums:
                    longest+=1
                    
                length = max(length, longest)
        return length

        