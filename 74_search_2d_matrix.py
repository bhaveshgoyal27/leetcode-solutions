class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while (l<=r):
            mid = (l+r)//2
            i, j = self.helper(mid, m, n)
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                l = mid+1
            else:
                r = mid-1
        return False

    def helper(self, mid, m , n):
        i, j = mid//n, mid%n
        return i, j
