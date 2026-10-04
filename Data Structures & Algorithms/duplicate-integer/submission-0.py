class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=0
        freq={}
        while i<len(nums):
            if nums[i] in freq:
                return True
            
            
            freq[nums[i]]=1
            i=i+1
        return False    