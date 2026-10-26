class Solution(object):
    def maxArea(self, height):
        maxwater=0
        i=0
        j=len(height)-1
        while i<j:
            width= j-i
            ht= min(height[i], height[j])
            current_water= width*ht
            maxwater = max(maxwater, current_water)
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
            

        return maxwater 
            


           
        