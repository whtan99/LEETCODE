class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = int((hi + lo) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return -1
