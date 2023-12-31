class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        for x in range(len(points)-1):
                seconds += max(abs(points[x][0] - points[x + 1][0]), abs(points[x][1] - points[x + 1][1]))
        return seconds