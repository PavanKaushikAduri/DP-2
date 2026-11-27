#This is coin change II problem

#Time complexity : O(m*n)
#space complexity : O(n)

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        m = len(coins)
        n = amount
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1,m+1):
            for j in range(0, n+1):
                if j - coins[i-1] >= 0:
                    dp[j] = dp[j] + dp[j - coins[i-1]]
        return dp[n]
