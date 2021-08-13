def arrSum(arr):
    result = 0

    for num in arr:
        result += num

    return result


def getDiagonal(matrix):
    # diagonal = [matrix[i][i] for i in range(0, len(matrix))]
    diagonal = []

    index = 0

    for row in range(0, len(matrix)):
        for i in range(0, len(matrix[row])):
            diagonal.append(matrix[row][index])
            index += 1
            break

    return arrSum(diagonal)


def getCounterDiagonal(matrix):
    # counter_diagonal = [matrix[i][~i] for i in range(0, len(matrix))]
    counter_diagonal = []

    index = len(matrix) - 1

    for row in range(0, len(matrix)):
        for i in range(0, len(matrix[row])):
            counter_diagonal.append(matrix[row][index])
            index -= 1
            break

    return arrSum(counter_diagonal)


matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
]

sum_diagonal = getDiagonal(matrix)
sum_counter_diagonal = getCounterDiagonal(matrix)

result = abs(sum_diagonal - sum_counter_diagonal)
print(result)
