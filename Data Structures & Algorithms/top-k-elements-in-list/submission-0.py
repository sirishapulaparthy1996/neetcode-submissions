class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = [[] for i in range(len(nums)+1)]
        n = {}
        res = []
        for i in nums:
            n[i] = 1 + n.get(i,0)
        for i, j in n.items():
            s[j].append(i)
        for i in range(len(s)-1, 0, -1):
            for j in s[i]:
                res.append(j)
                if len(res) == k:
                    return res







        
      