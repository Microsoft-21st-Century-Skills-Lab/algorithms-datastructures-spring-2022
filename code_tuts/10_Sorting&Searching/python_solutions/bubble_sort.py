def bubbleSort(array):
    # loop through each element of the array
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


#  Optimized solution
def optimized_bubble_sort(array):
    # loop through each element of the array
    for i in range(len(array)):
        # Keep track of swapping
        swapped = False
        # Loop to compare two adjacent elems
        for j in range(0, len(array) - i - 1):
            # to change to descending order alter the > to <
            if array[j] > array[j + 1]:
                # Swaps occur
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
        if not swapped:
            break  # We could as well break
    return array


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9, 90, -100, 95, 54, 23, 51, 67, 87, -4, 6, -23, -52, 12, 39, -95, 36, 41, 45, 94]
    # print(f'Sorted array in Ascending Order: {bubbleSort(data)}')
    print(f'Sorted array in Ascending Order Optimized Solution: {optimized_bubble_sort(data)}')
