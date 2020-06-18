# Number of Atoms

import sys
import re
from collections import Counter

'''

Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or
more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count
is greater than 1. If the count is 1, no digits will follow. For example, H2O
and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.
For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form:
the first name (in sorted order), followed by its count (if that count is more than 1),
followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

* All atom names consist of lowercase letters, except for the first character which is uppercase.
* The length of formula will be in the range [1, 1000].
* Formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.

'''

class Solution(object):
    def countOfAtoms(self, formula):
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
              stack[-1][name] += int(m1 or 1)
            if left_open:
              stack.append(Counter())
            if right_open:
                top = stack.pop()
                for k in top:
                  stack[-1][k] += top[k] * int(m2 or 1)

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))

tmp = Solution()

print(tmp.countOfAtoms("Mg(OH)2"))