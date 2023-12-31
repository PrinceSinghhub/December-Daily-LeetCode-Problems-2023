class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        seen = {}
        for i, c in enumerate(s):
            if c in seen: ans = max(ans, i - seen[c] - 1)
            seen.setdefault(c, i)
        return ans