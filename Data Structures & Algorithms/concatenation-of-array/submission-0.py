class Solution:
    def getConcatenation(self, nums):
        i=0
        
        ans=[]
        while i<2:
            j=0
            while j<len(nums):
                ans.append(nums[j])
                j=j+1
            i=i+1  
        return ans