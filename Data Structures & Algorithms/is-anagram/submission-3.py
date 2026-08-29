class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        if s_len != len(t):
            return False
        count = [0] * 26
        for s_char, t_char in zip(s, t):
            count[ord(s_char) - ord('a')] += 1
            count[ord(t_char) - ord('a')] -= 1

        return all(c == 0 for c in count)
