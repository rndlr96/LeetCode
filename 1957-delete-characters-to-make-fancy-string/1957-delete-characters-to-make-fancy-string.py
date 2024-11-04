class Solution:
    def makeFancyString(self, s: str) -> str:
        new_s = ''
        for idx in range(len(s)):
            if idx > 1 and s[idx-2] == s[idx-1] == s[idx]:
                continue
            new_s += s[idx]
        return new_s