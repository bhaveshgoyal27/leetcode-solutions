class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        r = set()
        res = set()
        for i in range(len(s)-9):
            a = s[i:i+10]
            if a in r:
                res.add(a)
            else:
                r.add(a)
        return list(res)