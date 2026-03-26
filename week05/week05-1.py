# week05-1.py
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums) 
        prefix = [0] 
        for i in range(N):
            prefix.append( prefix[-1] + nums[i] ) 
        postfix = [0] * (N+1)
        for i in range(N-1, -1, -1):
            postfix[i] = postfix[i+1] + nums[i]
        for i in range(N):
            if prefix[i] == postfix[i+1]: return i
        return -1















# Do not modify the lines below
nums = list(map(int, input()[1:-1].split(',') ))
print(Solution().pivotIndex(nums))