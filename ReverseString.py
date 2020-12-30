# Sum of Subsequence Widths

class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s

tmp = Solution()

print("Input: " + str(["H","a","n","n","a","h"]))

print("Output: " + str(tmp.reverseString(["H","a","n","n","a","h"])))