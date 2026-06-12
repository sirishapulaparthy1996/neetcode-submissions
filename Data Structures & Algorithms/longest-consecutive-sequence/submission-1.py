class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        l = 0
        for i in nums:
            l = 0
            if i - 1 not in nums:
                while i+l in nums:
                    l+=1
            longest = max(longest, l)
        return longest
                




        