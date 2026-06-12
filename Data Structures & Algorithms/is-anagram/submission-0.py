class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for i in s:
            a[i] = 1+a.get(i,0)
        for j in t:
            b[j] = 1+b.get(j,0)
        return a == b

        