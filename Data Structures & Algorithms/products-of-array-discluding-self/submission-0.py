class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * n
        right_prod = [1] * n

        left_prod[0] = nums[0]
        right_prod[n-1] = nums[n-1]
        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i]
            right_prod[n-i-1] = right_prod[n-i] * nums[n-i-1]

        res = []
        for i in range(n):
            if i == 0:
                res.append(right_prod[i+1])
            elif i == n-1:
                res.append(left_prod[i-1])
            else:
                res.append(left_prod[i-1] * right_prod[i+1])
        return res
