# Return true or false depending on the existence of the target element
def linear_search_element(my_array, target):
    if target in my_array:
        return True
    return False


# Return the index of the target if found
def linear_search(my_list, target):
    """

    :param my_list:- list of elements to search
    :param target: - the element to search
    :return: index of target element
    """
    for i in range(0, len(my_list)):
        if my_list[i] == target:
            return i
    return f'Does not exist'


if __name__ == '__main__':
    # print(linear_search([1, 4, 5, 675, 6], 8))
    # print(linear_search([1, 4, 5, 675, 6], 5))
    print(linear_search_element([1, 4, 5, 675, 6], 5))
