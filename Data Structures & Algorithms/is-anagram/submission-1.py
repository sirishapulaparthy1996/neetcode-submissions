class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_temp = {}
        t_temp = {}
        for i in s:
            s_temp[i] = 1 + s_temp.get(i,0)
        for j in t:
            t_temp[j] = 1 + t_temp.get(j,0)
        return s_temp == t_temp