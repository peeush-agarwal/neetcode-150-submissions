class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert_s_to_key(s):
            res = [0] * 26
            for c in s:
                res[ord(c) - ord('a')] += 1
            return tuple(res)

        groups = {}

        for s in strs:
            key = convert_s_to_key(s)
            groups[key] = groups.get(key, [])
            groups[key].append(s)
        
        return list(groups.values())
