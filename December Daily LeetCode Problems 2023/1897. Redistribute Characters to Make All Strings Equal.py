class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        StrLen = len(words)

        hasmap = {}

        for i in words:
            for j in i:
                if j not in hasmap:
                    hasmap[j] = 1
                else:
                    hasmap[j] += 1
        print(hasmap)
        for key,val in hasmap.items():
            if val % StrLen != 0:
                return False

        return True
