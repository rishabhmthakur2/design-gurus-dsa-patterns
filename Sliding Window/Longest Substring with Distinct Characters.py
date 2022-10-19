# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541027921_3Unit

"""
Given a string, find the length of the longest substring, which has all distinct characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".

Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""

# We again use an updating sliding window of non-fixed size
# We store the occurence of each character in a dictionary
# For each character, there should only be one occurence for that character to be in
# the window.
# If the occurence is 1, we expand our window.
# But if there is a repeating character, 

def longestSubstringLength(arr):
    characterCount= {}
    characterCount[arr[0]] = 1
    windowStart = 0
    windowEnd =0
    maxLength = 1
    while windowEnd < len(arr) - 1:
        # print(windowStart, windowEnd, characterCount)
        windowEnd += 1
        nextChar = arr[windowEnd]
        if nextChar in characterCount:
            while characterCount[nextChar] > 0:
                characterCount[arr[windowStart]] -= 1
                windowStart += 1
        
        characterCount[nextChar] = 1
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    return maxLength
                


# print(longestSubstringLength("abbbb"))
print(longestSubstringLength("tmmzuxt"))
print(longestSubstringLength("pwwkew"))
