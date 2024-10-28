import heapq

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        max_length = -1
        nums = list(set(nums))
        heapq.heapify(nums)
        num_dict = dict(zip(nums, [1]*len(nums)))

        while nums:
            current_value = heapq.heappop(nums)
            squre_value = current_value ** 2
            if num_dict.get(squre_value, 0):
                num_dict[squre_value] += num_dict[current_value]
                
        max_value = max(num_dict.values())
        
        return -1 if max_value == 1 else max_value