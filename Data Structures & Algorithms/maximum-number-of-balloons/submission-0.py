class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}

        i = 0
        while i < len(text):
            if text[i] in freq:
                freq[text[i]] += 1
            else:
                freq[text[i]] = 1
            i += 1

        if 'b' not in freq or 'a' not in freq or 'l' not in freq or 'o' not in freq or 'n' not in freq:
            return 0

        freq['l'] = freq['l'] // 2
        freq['o'] = freq['o'] // 2

        return min(
            freq['b'],
            freq['a'],
            freq['l'],
            freq['o'],
            freq['n']
        )