import random


def multiplier(argument):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = [num * argument for num in func(*args)]
            return result

        return wrapper

    return decorator


@multiplier(2)
def create_random_array(array_length):
    random_array = [random.randint(1, 10) for i in range(array_length)]
    print(random_array)
    return random_array


random_array = create_random_array(10)
print(random_array)
