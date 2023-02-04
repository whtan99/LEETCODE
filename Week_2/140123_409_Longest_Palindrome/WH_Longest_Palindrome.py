import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c1 = collections.Counter(s)
        ans = 0
        hasOdd = False
        for k in c1:
            if c1[k] % 2:
                hasOdd = True
                ans += c1[k] - 1
            else:
                ans += c1[k]
        if hasOdd:
            ans += 1
        return ans
