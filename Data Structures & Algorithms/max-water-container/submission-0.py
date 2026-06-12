class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxh = 0
        while l < r:
            a = ((r+1)-(l+1))*(min(heights[l],heights[r]))
            maxh = max(maxh, a)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxh
        


