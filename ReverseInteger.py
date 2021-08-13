def reverseInteger(num):
    as_string = str(num)

    if as_string[0] == "-":
        without_minus = as_string[1:]
        reversed_string_as_int = int(f"-{without_minus[::-1]}")
        return reversed_string_as_int
    else:
        reversed_number = as_string[::-1]
        return reversed_number


reversed_num1 = reverseInteger(-231)
print(reversed_num1)

reversed_num2 = reverseInteger(549)
print(reversed_num2)
