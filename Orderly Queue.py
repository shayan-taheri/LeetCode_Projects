# Orderly Queue

import sys

'''
A string S of lowercase letters is given.  Then, we may make any number of moves.

In each move, we choose one of the first K letters (starting from the left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.
'''

class Solution(object):
    def orderlyQueue(self, S, K):
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))

tmp = Solution()

print(tmp.orderlyQueue("cba", 1))