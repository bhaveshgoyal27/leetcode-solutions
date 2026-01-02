class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums)==0:
            return [-1,-1]
        l, r = 0, len(nums)-1
        lpos, rpos= -1,-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                lpos = mid
                r = mid-1
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid +1
        if lpos == -1:
            return [-1,-1]
        l,r = lpos, len(nums)-1
        while (l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                rpos = mid
                l = mid+1
            elif nums[mid]<target:
                l = mid+1
            else:
                r= mid-1
        return [lpos, rpos]
