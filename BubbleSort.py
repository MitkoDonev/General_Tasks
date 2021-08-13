def bubleSort(arr):
    for item in arr:
        for index in range(0, len(arr) - 1):
            if arr[index] > arr[index + 1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp


arr = [64, 34, 25, 12, 22, 11, 90]

bubleSort(arr)
print(arr)
