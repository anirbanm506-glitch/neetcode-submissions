class Solution(object):
    def isAnagram(self, s, t):
        need ={}
        have={}

        i=0
        while i < len(s):
            if s[i] in need:
                need[s[i]]+=1
            else:
                need[s[i]]=1
            i+=1
        
        i=0
        while i < len(t):
            if t[i] in have:
                have[t[i]]+=1
            else:
                have[t[i]]=1
            i+=1
        

        if len(need) != len(have):
            return False

        for char in need:
            if char not in have:
                return False

            if need[char] != have[char]:
                return False

        return True