def findPrimes(number):
    primes = []

    for num in range(number):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)

    return ", ".join(str(num) for num in primes)


result = findPrimes(35)
print(result)
