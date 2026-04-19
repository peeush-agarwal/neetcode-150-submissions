class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sum_i = {}

        for i in range(n):
            compl = target - nums[i]
            if compl in sum_i:
                return [sum_i[compl], i]
            sum_i[nums[i]] = i
        
        return [-1, -1]
