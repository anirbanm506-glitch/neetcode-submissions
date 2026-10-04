class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        i = 0

        while i < len(nums):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            i += 1

        majority = len(nums) // 2

        for num in freq:
            if freq[num] > majority:
                return num