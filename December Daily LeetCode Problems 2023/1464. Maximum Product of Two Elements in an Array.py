class Solution:
    def maxProduct(self, nums):
        modifidarr = []

        for i in nums:
            modifidarr.append(i - 1)

        modifidarr.sort()
        return modifidarr[-1] * modifidarr[-2]

