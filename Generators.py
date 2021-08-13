import random

character_list = [
    "a",
    "b",
    "c",
    "v",
    "f",
    "r",
    "t",
    "y",
    "u",
    "i",
    "o",
    "p",
    "q",
    "s",
    "d",
    "k",
    "l",
]

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def generator(char, number):
    result = []
    for i in range(5):
        result.append(f"test:{random.choice(char)}*{random.choice(number)}")

    yield result


result = generator(character_list, number_list)

for item in result:
    print(item)
