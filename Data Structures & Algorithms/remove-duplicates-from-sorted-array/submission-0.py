class Solution:
    def removeDuplicates(self,n):
        i=0
        k=1
        j=1

        while j<len(n):
            if(n[j]==n[j-1]):
                j=j+1
                continue

            n[i+1] = n[j]
            i=i+1
            k=k+1
            j=j+1

        return k    