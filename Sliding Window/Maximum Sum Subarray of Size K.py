# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1627871358579_1Unit

"""
Given an array of positive numbers and a positive number 'k'
find the maximum sum of any contiguous subarray of size 'k'.

Example: 
I/P: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
"""

# Non-optimized solution
# Calculate sum of each subarray of size k, keep a store of the max sum
def findMaximumSum(arr, k):
    maxSum = offset = 0
    while (offset + k - 1 < len(arr)):
        currentSum = sum(arr[offset : offset + k])
        maxSum = max(maxSum, currentSum)
        offset += 1
    return maxSum

print(findMaximumSum([2,1,5,1,3,12], 3))

# Optimized solution
# Use sliding window. At each iteration, subtract the outgoing element from window sum
# Add incoming element to window sum
# Compare window sum with max sum and store the highest
# This is optimized as we are resuing the sum of the last window

# TC: O(n)
# SC: O(1)

def findMaximumSumOptimized(arr, k):
    maxSum = currentSum = sum(arr[:k])
    for i in range(1, len(arr)- k + 1):
        currentSum -= arr[i-1]
        currentSum += arr[i + k - 1]
        maxSum = max(maxSum, currentSum)
    return maxSum


print(findMaximumSumOptimized([2,1,5,1,3,12], 3))
