# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
#
# A simple solution.
#
# 1. Use a list to save adjacent unique chars.
# 2. Iterate the string chars, if the char is in the list, remove chars before the specified char.

# start ->

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqs = []
        max_length = 0
        for c in s:
            if c in uniqs:
                max_length = max(len(uniqs), max_length)
                uniqs = uniqs[uniqs.index(c) + 1:]
            uniqs.append(c)
        max_length = max(len(uniqs), max_length)
        return max_length

# end <-


print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
