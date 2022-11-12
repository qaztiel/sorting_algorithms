"""Bubble Sort"""

unsorted = [8, 5, 3, 6, 9, 1, 2, 7, 4]
sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def bubble_sort(unsorted_list):
    sorted = False
    try:
        while not sorted:
            for index in range(len(unsorted_list)):
                if unsorted_list[index] > unsorted_list[index+1]:
                    # swap
                    unsorted_list[index], unsorted_list[index+1] = unsorted_list[index+1], unsorted_list[index]
    except IndexError:

    return unsorted_list



        

if __name__ == "__main__":
    print(bubble_sort(unsorted))