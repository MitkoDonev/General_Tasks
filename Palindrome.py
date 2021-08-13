text = "radkar"


def palindrome(text):
    middle = int(len(text) / 2)
    first = text[:middle]
    second = text[middle:]

    return first == second[::-1]


is_palindrome = palindrome(text)
print(is_palindrome)
