class Solution:
   
    def firstUniqChar(self, s):
        n = len(s)
        freq = {}
        
        # Count frequency of each character
        i = 0
        while i < n:
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
            i += 1
        
        # Find first character with frequency 1
        i = 0
        while i < n:
            if freq[s[i]] == 1:
                return i
            i += 1
        
        return -1