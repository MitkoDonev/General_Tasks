import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"Func {func.__name__} was executed for: {end - start}")

        return result

    return wrapper


@calculate_time
def calculate_factorial(number):
    if number < 0:
        return False

    fact = 1

    for i in range(1, number + 1):
        fact = fact * i

    return fact


result = calculate_factorial(325)
print(result)
