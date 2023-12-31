class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        # Initialize the maximum width to 0
        max_width = 0

        # Iterate through the sorted points
        for i in range(1, len(points)):
            # Calculate the width between consecutive points
            width = points[i][0] - points[i - 1][0]

            # Update the maximum width if the current width is greater
            max_width = max(max_width, width)

        return max_width
