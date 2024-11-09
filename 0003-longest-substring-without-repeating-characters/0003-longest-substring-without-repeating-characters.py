import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max_length = 0
        # for end in range(len(s), 0, -1):
        #     for start in range(end):
        #         if max_length > (end-start):
        #             break
        #         if len(set(s[start:end])) == (end-start):
        #             max_length = max(max_length, end-start)
        #             break
        # return max_length

        ch_set = set()
        start = 0
        max_length = 0
        for end in range(len(s)):
            while s[end] in ch_set:
                ch_set.remove(s[start])
                start += 1
            ch_set.add(s[end])
            max_length = max(max_length, end-start+1)
        return max_length