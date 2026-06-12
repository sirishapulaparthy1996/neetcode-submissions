class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = [[] for i in range(len(nums)+1)]
        p = {}
        t = []
        for i in nums:
            p[i] = 1 + p.get(i,0)
        for i, j in p.items():
            s[j].append(i)
        for i in range((len(s))-1, 0, -1):
            for m in s[i]:
                if len(t) < k:
                    t.append(m)
                else:
                    break
        return t

