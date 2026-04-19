class Solution:
    def is_anagram(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        count_s1 = {}
        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1
        
        for c in s2:
            if c not in count_s1:
                return False
            if count_s1[c] == 0:
                return False
            count_s1[c] -= 1
        
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        n = len(strs)
        taken = [False] * n

        for i in range(n):
            if taken[i]:
                continue
            
            taken[i] = True
            agrams = [strs[i]]
            for j in range(i+1, n):
                if taken[j]:
                    continue
                
                if self.is_anagram(strs[i], strs[j]):
                    agrams.append(strs[j])
                    taken[j] = True
            res.append(agrams)
        
        return res
