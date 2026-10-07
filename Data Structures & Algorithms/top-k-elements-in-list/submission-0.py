class Solution(object):
    def topKFrequent(self, nums, k):

        freq = {}

        i = 0
        while i < len(nums):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
            i += 1

        result = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        answer = []

        i = 0
        while i < k:
            answer.append(result[i][0])
            i += 1

        return answer