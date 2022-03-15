# !/bin/python3
# Author: Sebastian Opiyo
# Date Created: March 10, 2022
# Date Modified: March 10, 2022
# Descr: Implementing Selection sort algorithm

# A BRIEF OVERVIEW OF SELECTION SORT.
# ---------------------------------
"""
*
* The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
* In order to do this, a selection sort looks for the largest value as it makes a pass and,
* after completing the pass, places it in the proper location.
* 
"""


def selection_sort(alist: list) -> list:
    for to_fill_Slot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, to_fill_Slot + 1):
            # Changing from ascending to descending, change > to <
            if alist[location] < alist[position_of_max]:
                position_of_max = location

        # Swaps
        temp = alist[to_fill_Slot]
        alist[to_fill_Slot] = alist[position_of_max]
        alist[position_of_max] = temp
    return alist


if __name__ == '__main__':
    a_list = [2, 5, 7, 2, 78, 9, 43]
    print(selection_sort(a_list))
