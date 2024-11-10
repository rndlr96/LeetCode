class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        
        arrow = 1
        y = points[0][1]
        for idx in range(len(points)):
            if points[idx][0] > y:
                y = points[idx][1]
                arrow += 1

        return arrow
