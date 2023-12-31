class Solution:
    def transpose(self, matrix):
        res = list(zip(*matrix))
        return res