# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541018393_2Unit

"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can't skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

# Very similar to Longest Substring with K distinct elements
# We use a dynamic sliding window to iterate the entire fruits array in one pass
# We keep a count of unique fruit types we have (max can be 2)
# We keep expanding the window while the count <= 2
# We contract the window while our count is > 2

# TC: O(n)
# SC: O(1)


def findMaxNumberOfFruits(fruits):
    fruitCountPerType = {}
    maxFruitCount = 1
    windowStart = 0
    windowEnd = 0
    fruitCountPerType[fruits[0]] = 1
    while windowEnd < len(fruits) - 1:
        if len(fruitCountPerType) < 2:
            windowEnd += 1
            maxFruitCount = max(maxFruitCount, windowEnd - windowStart + 1)
            if fruits[windowEnd] not in fruitCountPerType:
                fruitCountPerType[fruits[windowEnd]] = 1
            else:
                fruitCountPerType[fruits[windowEnd]] += 1
        elif len(fruitCountPerType) == 2:
            windowEnd += 1
            if fruits[windowEnd] not in fruitCountPerType:
                fruitCountPerType[fruits[windowEnd]] = 1

            else:
                fruitCountPerType[fruits[windowEnd]] += 1
                maxFruitCount = max(maxFruitCount,
                                     windowEnd - windowStart + 1)
        elif len(fruitCountPerType) > 2:
            fruitCountPerType[fruits[windowStart]] -= 1
            if fruitCountPerType[fruits[windowStart]] == 0:
                del fruitCountPerType[fruits[windowStart]]
            windowStart += 1
    return maxFruitCount


print(findMaxNumberOfFruits(['A', 'B', 'C', 'A', 'C']))
print(findMaxNumberOfFruits(['A', 'B', 'C', 'B', 'B', 'C']))