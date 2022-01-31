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


print(linear_search([1,4,5,675,6], 8))