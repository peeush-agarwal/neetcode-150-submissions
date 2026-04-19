class Solution:
    def to_char_key(self, s: str) -> Tuple[str]:
        chars = [0] * 26
        for c in s:
            chars[ord(c) - 97] += 1
        
        return tuple(chars)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            k = self.to_char_key(s)
            groups[k] = groups.get(k, [])
            groups[k].append(s)
        return list(groups.values())
