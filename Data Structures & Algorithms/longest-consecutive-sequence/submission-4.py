class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            length = 1
            if i-1 not in nums:
                while i+1 in nums:
                    length += 1
                    i+=1
            longest = max(longest, length)
        return longest



        