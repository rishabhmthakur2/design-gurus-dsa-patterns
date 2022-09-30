# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628540999042_0Unit

"""
Given an array of positive numbers and a positive number 'S' 
Find the length of the smallest contiguous subarray whose sum 
is greater than or equal to 'S'. 

Return 0 if no such subarray exists.

I/P: [2, 1, 5, 2, 3, 2], S=7 
O/P: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
"""
# Optimized solution
# Uses sliding window to iterate through the entire array in one pass
# Keep expanding the window while the sum is < S
# When sum is >= S, eliminate the left hand eliminate from the window

# TC: O(n)
# SC: O(1)


def findSmallestSubarrayLength(arr, S):
    windowStart = 0
    windowEnd = 0
    smallestLength = len(arr)
    while windowEnd < len(arr):
        currentSum = 0
        if windowStart == windowEnd:
            currentSum = arr[windowStart]
        else:
            currentSum = sum(arr[windowStart:windowEnd + 1])

        if currentSum < S:
            windowEnd += 1
        else:
            smallestLength = min(smallestLength, windowEnd - windowStart + 1)
            windowStart += 1
    return smallestLength


print(findSmallestSubarrayLength([2, 1, 5, 2, 3, 2], 7))
print(findSmallestSubarrayLength([3, 4, 1, 1, 6], 8))
print(findSmallestSubarrayLength([2, 1, 5, 2, 8], 7))
