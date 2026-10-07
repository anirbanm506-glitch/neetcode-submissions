class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        need = {}
        have = {}

        # Count ransomNote
        i = 0
        while i < len(ransomNote):
            if ransomNote[i] in need:
                need[ransomNote[i]] += 1
            else:
                need[ransomNote[i]] = 1
            i += 1

        # Count magazine
        i = 0
        while i < len(magazine):
            if magazine[i] in have:
                have[magazine[i]] += 1
            else:
                have[magazine[i]] = 1
            i += 1

        # Compare counts
        for char in need:
            if char not in have:
                return False

            if have[char] < need[char]:
                return False

        return True