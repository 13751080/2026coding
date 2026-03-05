# LeetCode 1431. Kids With the Greatest Number of Candies
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        best=max(candies)









# Do not remove below lines
candies = list(map(int, input()[1:-1].split(',') ))
extraCandies = int(input())
print(Solution().kidsWithCandies(candies, extraCandies))
