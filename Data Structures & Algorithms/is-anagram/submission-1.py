class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def _count_dict(arr):
            res = {}
            for i in arr:
                res[i] = res.get(i, 0) + 1
            return res
        s_set = _count_dict(s)
        t_set = _count_dict(t)
        
        for i in s:
            if i not in t_set:
                return False
            elif t_set[i] == 0:
                return False
            else:
                t_set[i] -= 1
        return True
