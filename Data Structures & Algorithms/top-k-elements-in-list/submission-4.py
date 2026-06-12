class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = [[] for i in range(len(nums) + 1)]
        nums_ = {}
        for i in nums:
            nums_[i] = 1 + nums_.get(i,0)
        for i, j in nums_.items():
            s[j].append(i)
        t = []
        for i in range(len(s)-1, 0, -1):
            for j in s[i]:
                t.append(j)    
                if len(t) == k:
                    return t


