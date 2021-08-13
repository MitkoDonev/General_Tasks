def simpleArraySum(arr):
    result = 0

    for num in arr:
        result += num

    return result


arr = [1, 2, 3, 4, 10, 11]

result = simpleArraySum(arr)
print(result)
