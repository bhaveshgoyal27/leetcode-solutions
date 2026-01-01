class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        res = []
        n = len(code)
        if k>0:
            for i in range(n):
                a1 = (i+1)%n
                a2= (i+1+k)%n
                if a1<=a2:
                    res.append(sum(code[a1:a2]))
                else:
                    res.append(sum(code[a1:])+ sum(code[:a2]))
        else:
            k*=-1
            for i in range(n):
                a1 = (i-1)%n
                a2= (i-1-k)%n
                if a2<=a1:
                    res.append(sum(code[a2+1:a1+1]))
                else:
                    res.append(sum(code[:a1+1])+ sum(code[a2+1:]))
        return res
