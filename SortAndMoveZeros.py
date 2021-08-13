array = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4, 0, 99]


def countZeros(array):
    count = 0
    for num in array:
        if num == 0:
            count += 1

    return count


def removeZeros(numbers):
    return [i for i in numbers if i != 0]


def appendZeros(numbers, count):
    added_zerors = numbers

    for i in range(count):
        added_zerors.append(0)

    return added_zerors


def moveZeros(numbers):

    zero_count = countZeros(numbers)

    removed_zeros = removeZeros(numbers)

    removed_zeros.sort()

    arranged_numbers = appendZeros(removed_zeros, zero_count)

    return arranged_numbers


result = moveZeros(array)
print(result)
