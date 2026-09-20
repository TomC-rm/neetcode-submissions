class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n= len(s)
        if n != len(t):
            return False
        
        counts = [0] * 26
        for s_char, t_char in zip(s, t):
            counts[ord(s_char) - ord('a')] += 1
            counts[ord(t_char) - ord('a')] -= 1
        
        return all(count == 0 for count in counts)
