# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541009794_1Unit

"""
Given a string, find the length of the longest substring in it with no more than 
K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

# We use sliding window again to iterate over the entire array in one pass
# Using HasMap/Dictionary - we keep a track of all the elements (unique) in the window
# We keep resizing the window based on the number of unique characters in the window

# TC: O(n)
# SC: O(k)


def findLongestSubstring(arr, k):
    characterDict = {}
    longestLength = 1
    windowStart = 0
    windowEnd = 0
    characterDict[arr[0]] = 1
    while windowEnd < len(arr) - 1:
        if len(characterDict) < k:
            windowEnd += 1
            longestLength = max(longestLength, windowEnd - windowStart + 1)
            if arr[windowEnd] not in characterDict:
                characterDict[arr[windowEnd]] = 1
            else:
                characterDict[arr[windowEnd]] += 1
        if len(characterDict) == k:
            windowEnd += 1
            if arr[windowEnd] not in characterDict:
                characterDict[arr[windowEnd]] = 1
            else:
                characterDict[arr[windowEnd]] += 1
                longestLength = max(longestLength, windowEnd - windowStart + 1)
        if (len(characterDict) > k):
            characterDict[arr[windowStart]] -= 1
            if characterDict[arr[windowStart]] == 0:
                del characterDict[arr[windowStart]]
            windowStart += 1
    return longestLength

print(findLongestSubstring("araaci", 2))
print(findLongestSubstring("araaci", 1))
print(findLongestSubstring("cbbebi", 3))
