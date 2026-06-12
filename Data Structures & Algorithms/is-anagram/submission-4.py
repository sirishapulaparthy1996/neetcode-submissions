class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sp = {}
        tp = {}
        for i in range(len(s)):
            sp[s[i]] = sp.get(s[i], 0) + 1
        for j in range(len(t)):
            tp[t[j]] = tp.get(t[j], 0) + 1
        for i, j in sp.items():
            if sp[i] != tp.get(i, 0):
                return False
        return True

            

        