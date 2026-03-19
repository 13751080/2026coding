# week04-1.py
from typing import *
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums) 
        total = sum( nums[:k] )
        maxTotal = total
        for i in range(k, N): 
            total = total + nums[i] - nums[i-k]
            maxTotal = max(maxTotal, total)
        return maxTotal / k










# Do not modify the lines below
nums = list(map(int, input()[1:-1].split(',') ))
k = int(input())
print(f'{Solution().findMaxAverage(nums, k):.5f}' )