class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        def is_prime(num) -> bool:
            for idx in range(2, int(math.sqrt(num))+1):
                if num % idx == 0:
                    return False
            return True
        
        for idx in range(len(nums)):
            max_sub = nums[0] if idx == 0 else nums[idx] - nums[idx-1]
            
            if max_sub <= 0:
                return False
            
            for prime_cand in range(max_sub-1, 1, -1):
                if is_prime(prime_cand):
                    nums[idx] = nums[idx] - prime_cand
                    break
        
        return True