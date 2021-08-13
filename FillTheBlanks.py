numbers = [1, None, 2, 5, None, None, 5, None]


def findDiffernece(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] != None and arr[i + 1] != None:
            return abs(arr[i] - arr[i + 1])


def fillBlanks(arr):
    difference = findDiffernece(arr)

    for i in range(0, len(arr)):
        if arr[i] is None:
            arr[i] = arr[i - 1] + difference

    return arr


result = fillBlanks(numbers)
print(result)
