'''
Following the brute force method, Initially I am sorting the array and returning k-1 element as output as indexing starts from 0 in python
As per the given examples, we can say that duplicate elements will be present
Given: arr = [1, 5, 12, 3, 11, 5], k = 3
Result: 5 as the first two smaller numbers are [1, 3]


Given: arr = [1, 7, 12, 2, 11, 7], k = 4
Result: 7 as the first three smaller numbers are [1, 2, 7]


Given: arr = [5, 12, 11, -2, 12], k = 3
Result: 11 as the first two small numbers are [5, -2]
'''
def findkthSmallest(arr,k):
    # sorting the array
    arr.sort()
    # return the kth smallest element
    return arr[k-1]

print(findkthSmallest([1, 7, 12, 2, 11, 7],4)) # output is 7
print(findkthSmallest([5, 12, 11, -2, 12],3)) # output is 11
print(findkthSmallest([-5, -2, 0, -1, 1],2))  # output is -2