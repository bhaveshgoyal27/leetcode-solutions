class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float("inf")
        n = len(nums)
        if n<=l:
            s= sum(nums)
            if s>0:
                return s
            else:
                return -1
        for i in range(n-l+1):
            curr_sum = sum(nums[i:i+l])
            if curr_sum>0:
                min_sum = min(min_sum, curr_sum)
            j=l
            while j<r and i+j<n:
                curr_sum+= nums[i+j]
                if curr_sum>0:
                    min_sum = min(min_sum, curr_sum)
                j+=1
        if min_sum == float("inf"):
            return -1
        else:
            return min_sum