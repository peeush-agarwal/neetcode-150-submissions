class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            k = tuple(sorted(s))
            groups[k] = groups.get(k, [])
            groups[k].append(s)
        
        return list(groups.values())
