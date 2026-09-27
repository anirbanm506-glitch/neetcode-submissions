class Solution:
    def twoSum(self, n, target):
        i=0
        j=len(n)-1

        while i<j:
            sum=n[i] + n[j]
            
            if(sum == target):
                return [i + 1, j + 1]
            elif(sum < target):
                i = i + 1
            elif(sum > target):
                j = j - 1