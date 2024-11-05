import heapq

class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if len(self.right) == 0 or -self.right[0] >= num:
            heapq.heappush(self.right, -num)
        else:
            heapq.heappush(self.left, num)

        # Balance the heaps
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(
                self.left, -heapq.heappop(self.right)
            )
        elif len(self.right) < len(self.left):
            heapq.heappush(
                self.right, -heapq.heappop(self.left)
            )

    def findMedian(self) -> float:
        if len(self.right) == len(self.left):
            return (-self.right[0] + self.left[0]) / 2.0
        else:
            return -self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()