import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c1 = collections.Counter(nums)
        for k in c1:
            if c1[k] > len(nums) / 2:
                return k
