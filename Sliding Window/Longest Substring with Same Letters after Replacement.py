# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541037657_4Unit

"""
Given a string with lowercase letters only, if you are allowed to replace no more than 'k' 
letters with any letter, find the length of the longest substring having the same letters after replacement.

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

# We use a sliding window to complete the solution in one pass
# For each pass, we move the window end to the right
# We check if the non-repeating characters (if any) have a count > k
# If yes, we shrink the window from left.
# For each pass, we check the max repeat count of any character and also the max length of the window 
def longestSubstring(arr, k):
    windowStart = 0
    windowEnd = 0
    maxRepeatCount = 0
    characterCount = {}
    maxLength = 0
    while windowEnd < len(arr):
        nextChar = arr[windowEnd]
        if nextChar not in characterCount:
            characterCount[nextChar] = 0

        characterCount[nextChar] += 1

        maxRepeatCount = max(maxRepeatCount, characterCount[nextChar])

        if (windowEnd - windowStart + 1 - maxRepeatCount) > k:
            firstChar = arr[windowStart]
            characterCount[firstChar] -= 1
            windowStart += 1

        maxLength = max(maxLength, windowEnd - windowStart + 1)
        windowEnd += 1
    return maxLength

print(longestSubstring("aabccbb",2))
print(longestSubstring("abbcb",1))
print(longestSubstring("abccde",1))
