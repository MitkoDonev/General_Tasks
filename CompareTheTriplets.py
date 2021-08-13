def scoreCalculator(arr1, arr2):
    arr1_result = 0
    arr2_result = 0

    for index in range(len(arr1)):
        if arr1[index] > arr2[index]:
            arr1_result += 1
        elif arr1[index] < arr2[index]:
            arr2_result += 1

    return arr1_result, arr2_result


first_arr = [17, 28, 30]
second_arr = [99, 16, 8]

result1, result2 = scoreCalculator(first_arr, second_arr)

print(result1, result2)
