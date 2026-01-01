class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            c0 = 0
            c1 = 0
            j = i
            for j in range(i,n):
                if s[j]=="0":
                    c0+=1
                else:
                    c1+=1
                if c1>k and c0>k:
                    break
                count+=1
        return count