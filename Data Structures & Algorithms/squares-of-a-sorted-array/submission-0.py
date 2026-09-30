class Solution:
    from typing import List

    def sortedSquares(self, nums: List[int]) -> List[int]:

        neg = []
        pos = []

        # Separate negative and positive numbers
        i = 0
        while i < len(nums):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
            i += 1

        # Case 1: No negative numbers
        if len(neg) == 0:
            res = []
            i = 0

            while i < len(pos):
                res.append(pos[i] * pos[i])
                i += 1

            return res

        # Case 2: No positive numbers
        if len(pos) == 0:
            res = []
            i = 0

            while i < len(neg):
                res.append(neg[i] * neg[i])
                i += 1

            res.reverse()
            return res

        # Square negative numbers
        i = 0
        while i < len(neg):
            neg[i] = neg[i] * neg[i]
            i += 1

        # Reverse negative squares
        neg.reverse()

        # Square positive numbers
        i = 0
        while i < len(pos):
            pos[i] = pos[i] * pos[i]
            i += 1

        # Merge two sorted arrays
        n = len(neg)
        m = len(pos)

        res = []

        i = 0
        j = 0

        while i < n and j < m:

            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1

        # Remaining negative squares
        while i < n:
            res.append(neg[i])
            i += 1

        # Remaining positive squares
        while j < m:
            res.append(pos[j])
            j += 1

        return res