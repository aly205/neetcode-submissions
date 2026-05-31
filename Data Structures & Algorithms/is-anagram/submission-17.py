class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = dict()
        t_chars = dict()
        for a in s:
            s_chars[a] = s_chars.get(a, 0) + 1
        for b in t:
            t_chars[b] = t_chars.get(b, 0) + 1

        return s_chars == t_chars

        