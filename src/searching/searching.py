def linear_search(arr, target):
    # Your code here

    # Walk through all the items and compare them with the target.
    for i in range(0,len(arr)):
        # if a match, break the loop.
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    # Set the left and right frontiers.

    left = 0
    right = len(arr) - 1
 
    while left <= right:

        # Find the mid point:

        mid = (right + left) // 2

        if target == arr[mid]:
            return mid
        
        # if the target is on the left, move to the left

        elif target < arr[mid]:
            right -=1

        # otherwise move to the right

        else:
            left +=1
    
    # if you kept moving and no value where found, set -1 as a return value

    return -1  # not found

if __name__ == "__main__":
    print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9],9))
