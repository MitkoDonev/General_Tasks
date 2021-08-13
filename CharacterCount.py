first = "alphabet"
second = "barbbbbados"


def characterCount(text):
    frequency = {}

    for character in text:
        if character not in frequency:
            frequency[character] = 1
        else:
            frequency[character] += 1

    for key, value in frequency.items():
        print(f"Key: {key} / Value: {value}")


characterCount(first)
characterCount(second)
