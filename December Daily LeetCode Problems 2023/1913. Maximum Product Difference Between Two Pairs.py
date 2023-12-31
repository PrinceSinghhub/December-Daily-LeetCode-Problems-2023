class Solution:
    def maxProductDifference(self, nums):
        nums.sort()

        a, b = nums[-1], nums[-2]
        c, d = nums[0], nums[1]

        ans = (a * b) - (c * d)
        return ans