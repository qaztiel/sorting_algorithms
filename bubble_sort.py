"""
Bubble Sort
O(n^2)
"""

unsorted = [8, 5, 3, 6, 9, 1, 2, 7, 4]
sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def bubble_sort(unsorted_list):
    sorted = False

    while not sorted:
        swapped = False
        for index in range(len(unsorted_list)):
            if (index+1 < len(unsorted_list)) and (unsorted_list[index] > unsorted_list[index+1]):
                unsorted_list[index], unsorted_list[index+1] = unsorted_list[index+1], unsorted_list[index]
                swapped = True
        
        if not swapped:
            sorted = True
 
    return unsorted_list


"""geeksforgeeks.org"""
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        

if __name__ == "__main__":
    if (bubble_sort(unsorted) == sorted):
        print("Successful")
        print(bubble_sort(unsorted), print(sorted))

    print(bubbleSort(unsorted))
    print(unsorted)
