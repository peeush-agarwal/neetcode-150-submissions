class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = {}
        for n in nums:
            cnts[n] = cnts.get(n, 0) + 1
        
        cnts_ordered = sorted(cnts, key=cnts.get, reverse=True)

        return cnts_ordered[:k]
