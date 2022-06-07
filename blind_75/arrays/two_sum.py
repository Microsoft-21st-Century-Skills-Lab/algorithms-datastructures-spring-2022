# Naive approach

def two_sum(nums_array: list, target: int):
    """Time complexity: O(n^2)"""
    array_length = len(nums_array)
    for i in range(array_length):
        for j in range(array_length):
            if i == j:  # i & j at the same position
                continue
            if nums_array[i] + nums_array[j] == target:
                return [i, j]
            if nums_array[i] + nums_array[j] > target:
                break
    return []


def optimized_nums_array(nums: list, target: int):
    # We are going to employ two pointer strategy
    # This strategy works on a sorted array
    """Time complexity: O(n)"""
    i = 0
    j = len(nums) - 1

    while (i < j):
        if nums[i] + nums[j] == target:  # Checks consecutive elements in  a list
            return [i, j]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return []


# A naive strategy that works for unsorted array
def optim_nums_unsorted_array(nums: list, target: int):
    list_len = len(nums)

    for i in range(list_len - 1):
        if nums[i] + nums[i + 1] == target:
            return [i, i + 1]
        else:
            i += 1
    return []


# Use of a hashtable
# Assuming the input array has integers only
# 1. Create a hashmap which accepts integer datatype as key & value
# 2. Iterate through each element in the given array starting from the 1st elem
# 3. In each iteration check if required number(required_num = target_sum - current_number) is present in hashmap
# 4. If present, return [required_number_index, current_number_index] as result
# 5. Otherwise add the current iteration number as key & its index as value to the hashmap.
# Repeat the procedure until you find the result.
def two_sum_hashmap_solution(nums: list, target: int):
    existing = {}
    for i in range(len(nums)):
        required_num = target - nums[i]
        if required_num in existing:
            return [i, existing[required_num]]
        else:
            existing[nums[i]] = i
    return []


if __name__ == '__main__':
    nums = [7, 2, 13, 11]
    # print("Naive solution")
    # print(two_sum(nums, 9))
    # print("Optimized solution")
    # print(optimized_nums_array(nums, 24))
    # print(optim_nums_unsorted_array(nums, 24))
    print(two_sum_hashmap_solution(nums, 24))
