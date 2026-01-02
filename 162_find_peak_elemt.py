class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        nums.append(float("-inf"))
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = right - 1

        return mid