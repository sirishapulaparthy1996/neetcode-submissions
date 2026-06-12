class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = [[] for i in range(len(nums)+1)]
        s = {}
        t = []
        for i in range(len(nums)):
            s[nums[i]]=1+s.get(nums[i], 0)
        for i,j in s.items():
            x[j].append(i)
        for i in x[len(x)-1:0:-1]:
            for j in i:
                if len(t)< k:
                    t.append(j)
        return t


            

        