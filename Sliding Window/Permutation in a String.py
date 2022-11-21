# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541055153_6Unit

"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has 'n' distinct characters, it will have n!n! permutations.

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""

# Unoptimized method

# We will use a sliding window to go through the entire array in one pass
# We first create a Counter to keep a count of all character occurences for the pattern string
# We then set the window length to the length of the pattern string
# For each window, we check if the counter for that window matches the counter for the pattern

from collections import Counter


def checkPatternPermutationInString(string, pattern):
    windowStart = 0
    windowEnd = len(pattern) - 1
    patternCounter = dict(Counter(pattern))
    while windowEnd < len(string):
        currentString = string[windowStart:windowEnd + 1]
        currentCounter = dict(Counter(currentString))
        if currentCounter == patternCounter:
            return True
        windowStart += 1
        windowEnd += 1
    return False
print(checkPatternPermutationInString("oidbcaf", "abc"))

# Optimized Method

def permutationInAString(s1, s2):
    if s1 == s2:
            return True
        
    if s1 == "" or len(s1) == 0:
        return True
    
    if len(s1) > 0 and len(s2) == 0:
        return False
    
    start = 0
    end = 0

    s1Counter = {}
    for char in s1:
        if char not in s1Counter:
            s1Counter[char] = 0
        s1Counter[char] += 1
    
    windowCounter = {}
    while end < len(s2):
        char = s2[end]
        if char not in s1Counter:
            windowCounter = {}
            end += 1
            start = end
            continue

        if char in windowCounter:
            if windowCounter[char] + 1 > s1Counter[char]:
                if start == end:
                    end += 1
                    start = end
                    windowCounter = {}
                else:
                    windowCounter[s2[start]] -= 1
                    start += 1
                continue
        
        if char not in windowCounter:
            windowCounter[char] = 0
        
        windowCounter[char] += 1

        end += 1

        if windowCounter == s1Counter:
            return True
        
    return False