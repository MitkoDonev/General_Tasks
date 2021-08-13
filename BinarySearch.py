import random

random_list = [random.randrange(1, 10000, 1) for i in range(5000)]
random_list.sort()


def searchNum(arr, num):
    middle_index = int(len(arr) / 2)

    if middle_index == 0:
        return False
    elif arr[middle_index] == num:
        return True
    elif num < arr[middle_index]:
        return searchNum(arr[:middle_index], num)
    elif num > arr[middle_index]:
        return searchNum(arr[middle_index:], num)

    return False


to_find = random_list[500]  # always return True
to_check = 7542

is_present = searchNum(random_list, to_check)
print(is_present)
