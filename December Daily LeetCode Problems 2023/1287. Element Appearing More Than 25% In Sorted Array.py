class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        per = len(arr) // 4

        for i in arr:
            if arr.count(i) > per:
                return i
        return -1