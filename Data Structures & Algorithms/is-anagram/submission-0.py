class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_set = set(s)
        t_set = set(t)
        return s_set == t_set
