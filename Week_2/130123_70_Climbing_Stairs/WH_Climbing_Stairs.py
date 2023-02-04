class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 1
        memo[1] = 1
        def helper(num):
            if num in memo:
                return memo[num]
            ans = helper(num - 1) + helper(num - 2)
            memo[num] = ans
            return ans


        return helper(n)
