class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def is_nice(sub: str) -> bool:
            return all(c.lower() in sub and c.upper() in sub for c in sub)
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                substr = s[start:start + length]
                if is_nice(substr):
                    return substr
    
        return ""