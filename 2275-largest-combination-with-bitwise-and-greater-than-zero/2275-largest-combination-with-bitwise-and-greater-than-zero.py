import collections

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        result = 0
        for i in range(24):
            count = sum(1 for candidate in candidates if candidate & (1 << i))
            result = max(result, count)
        return result