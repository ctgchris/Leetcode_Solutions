class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxArea=0

        l=0
        r=len(height)-1

        while l<r:
            
            currArea=((r-l)) * min(height[l], height[r])
            maxArea=max(currArea, maxArea)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return maxArea
