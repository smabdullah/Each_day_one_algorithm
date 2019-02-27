"""
A Python program to implement a Maximum-subarray problem using Divide and Conquer 
S M Abdullah (sma.csedu@gmail.com)
27-02-2019

The aim of this program is to find the maximum subarray from an array of values.
"""

# Importing library
import math

def findMaxCrossingSubArray(A, low, mid, high):
    leftSum = -math.inf
    sums = 0
    maxLeft = 0
    for i in range(mid,low+1,-1):
        sums = sums + A[i]
        if sums > leftSum:
            leftSum = sums
            maxLeft = i
    rightSum = - math.inf
    sums = 0
    maxRight = 0
    for j in range(mid+1,high+1):
        sums = sums + A[j]
        if sums > rightSum:
            rightSum = sums
            maxRight = j
    return [maxLeft, maxRight,leftSum+rightSum]

def findMaximumSubArray(A, low, high):
    if high == low:
        # base-case. Only one item in the list
        return [low, high, A[low]]
    else:
        # divide the list into two parts
        mid = (low+high)//2
    leftResult = findMaximumSubArray(A,low,mid)
    rightResult = findMaximumSubArray(A, mid+1, high)
    # the maximum is crossing between two parts
    crossResult = findMaxCrossingSubArray(A, low, mid, high)
    if leftResult[2] >= rightResult[2] and leftResult[2] >= crossResult[2]:
        return leftResult
    elif rightResult[2] >= leftResult[2] and rightResult[2] >= crossResult[2]:
        return rightResult
    else:
        return crossResult
# test data
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
result = findMaximumSubArray(A, 0, len(A)-1)
print('The optimal subarray is from index {:d} to index {:d} is {:d}'.format(result[0]+1, result[1]+1, result[2]))
