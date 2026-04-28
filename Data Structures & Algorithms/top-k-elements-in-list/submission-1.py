class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        cnts = {}
        for n in nums:
            cnts[n] = cnts.get(n, 0) + 1
        
        top_k = heapq.nlargest(k, cnts, key=cnts.get)

        return top_k
