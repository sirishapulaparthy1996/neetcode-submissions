class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_reversed = ''
        for i in s:
            if i.isalnum():
                s_reversed+=i.lower()
        return s_reversed == s_reversed[::-1]

        