"""
A Python program to implement a Maximum-subarray problem using Divide and Conquer 
S M Abdullah (sma.csedu@gmail.com)
27-02-2019

The aim of this program is to find the maximum subarray from an array of values.

04/03/2019: Function and variable names are updated following PEP 8
"""

# Importing library
import math

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -math.inf
    sums = 0
    max_left = 0
    for i in range(mid, low+1, -1):
        sums = sums + A[i]
        if sums > left_sum:
            left_sum = sums
            max_left = i
    right_sum = - math.inf
    sums = 0
    max_right = 0
    for j in range(mid+1, high+1):
        sums = sums + A[j]
        if sums > right_sum:
            right_sum = sums
            max_right = j
    return [max_left, max_right, left_sum + right_sum]

def find_maximum_subarray(A, low, high):
    if high == low:
        # base-case. Only one item in the list
        return [low, high, A[low]]
    else:
        # divide the list into two parts
        mid = (low + high) // 2
    left_result = find_maximum_subarray(A, low, mid)
    right_result = find_maximum_subarray(A, mid+1, high)
    # the maximum is crossing between two parts
    cross_result = find_max_crossing_subarray(A, low, mid, high)
    if left_result[2] >= right_result[2] and left_result[2] >= cross_result[2]:
        return left_result
    elif right_result[2] >= left_result[2] and right_result[2] >= cross_result[2]:
        return right_result
    else:
        return cross_result
# test data
A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
result = find_maximum_subarray(A, 0, len(A) - 1)
print('The optimal subarray is from index {:d} to index {:d} is {:d}'.format(result[0] + 1, result[1] + 1, result[2]))
