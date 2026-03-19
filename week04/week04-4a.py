# week04-4a.py 重寫學習計畫 Prefix Sum 第1題
# LeetCode 1732. Find the Highest Altitude
# 找到最高的海拔高度( 一直加, 就好了!!! )
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 # 一開始的高度是0
        for gg in gain : # Python 進階 for 迴圈: 依序取出 gg
            H += gg
            ans = max(ans, H)
        return ans
        
        N = len(gain) # 陣列的長度 N
        ans = H = 0 # 一開始的高度是0
        # 答案一開始是0, 因為一開始的高度是0
        for i in range(N): # 逐個加起來
            H += gain[i] # 現在增減的是 gain[i] 加進 H
            ans = max(ans, H) # 更新最高的答案
        return ans