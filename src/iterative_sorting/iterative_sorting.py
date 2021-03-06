def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
      
        for j in range(cur_index,len(arr)) :
            if arr[j] < arr[cur_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    count = None
    while count!= 0:
        count = 0
        for i in range(0,len(arr)-1):
            
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here

    # count = array of maximun + 1 zeros
    if [1 for x in arr if x < 0] != []:
    
        return f'Error, negative numbers not allowed in Count Sort'

    elif arr != []:

        maximum = max(arr)
    
        count = [0] * (maximum + 1)

        # for x in input do
        #     count[key(x)] += 1

        for i in range(0,len(arr)):
            count[arr[i]] +=1

        # Sum the previous entry to the count array

        
        for i in range(1,len(count)):
            count[i] = count[i-1] + count[i]

        print(count)

        # output = array of the same length as input

        output = [None] * len(arr)

        # for x in input do
        #     output[count[key(x)]] = x
        #     count[key(x)] += 1 

        for i in range(1,len(arr)+1):

            output[count[arr[-i]] - 1] = arr[-i]
            count[arr[-i]] -= 1

        return output

    else:

        return arr

if __name__ == "__main__":
    print(counting_sort([1, 3, -2, 4, 5]))