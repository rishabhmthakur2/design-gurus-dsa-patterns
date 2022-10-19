# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541045705_5Unit

"""
Given an array containing 0s and 1s, if you are allowed to replace no more 
than 'k' 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""

def longestSubarrayLength(arr, k):
    windowStart, windowEnd, maxLength, countZeros, countOnes = 0, 0, 0, 0, 0

    while windowEnd < len(arr):
        nextElement = arr[windowEnd]

        if nextElement == 1:
            countOnes += 1
        
        else:
            countZeros += 1
        
        if countZeros > k:
            firstElement = arr[windowStart]
            if firstElement == 1:
                countOnes -= 1
            else:
                countZeros -= 1
            windowStart += 1
        
        maxLength = max(maxLength, windowEnd - windowStart + 1)
        windowEnd += 1
    
    return maxLength

print(longestSubarrayLength([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(longestSubarrayLength([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
print(longestSubarrayLength([1, 0, 0, 1, 0, 1, 0, 1 ], 2))

