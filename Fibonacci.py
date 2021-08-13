def fibonacci(num):

    if num <= 0:
        print("Plese enter positive number")

    data = [0, 1]
    if num > 2:
        for i in range(2, num):
            data.append(data[i - 1] + data[i - 2])

    return data


result = fibonacci(10)
print(result)
