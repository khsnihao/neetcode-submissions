class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for num in nums:
            if num:
                prod *= num
            else:
                zeros += 1
        # if there are more than one zero in a list, the rest will all be 0s
        if zeros > 1: return [0] * len(nums)

        res = [0]*len(nums)
        for i, c in enumerate(nums):
            if zeros:
                if c: # rest except value = 0
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod // c
        return res
