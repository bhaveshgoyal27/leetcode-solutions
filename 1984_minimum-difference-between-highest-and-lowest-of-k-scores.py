class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        m = float("inf")
        for i in range(len(nums)-k+1):
            diff = nums[i + k - 1] - nums[i]
            m = min(m, diff)
            if m == 0:
                return 0
        return m