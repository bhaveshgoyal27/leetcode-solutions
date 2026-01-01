class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        d = str(num)
        res = 0
        current_number = int(d[:k])
        for i in range(len(d)-k+1):
            if current_number!=0 and num%current_number==0:
                res+=1
            if i + k < len(d):
                current_number = current_number * 10 + int(d[i + k]) - int(d[i]) * 10**k
        return res
