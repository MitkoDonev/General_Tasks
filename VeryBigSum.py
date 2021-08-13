def bigSum(arr):
    result = 0

    for num in arr:
        result += num

    return result


arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

result = bigSum(arr)
print(result)
