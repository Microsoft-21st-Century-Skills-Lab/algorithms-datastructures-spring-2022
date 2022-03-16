def insertion_sort(array: list) -> list:
    for index in range(1, len(array)):

        current_value = array[index]
        position = index

        while position > 0 and array[position - 1] > current_value:
            # Shift to the right to create space
            array[position] = array[position - 1]
            position = position - 1

        array[position] = current_value


if __name__ == '__main__':
    a_list = [2, 5, 7, 2, 78, 9, 43]
    insertion_sort(a_list)
    print(a_list)
