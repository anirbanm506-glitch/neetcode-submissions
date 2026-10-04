class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        i=0
        freq={}
        while i<len(nums):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
            i+=1

        for num in freq:
            if freq[num] > len(nums)/2:
                return num
                