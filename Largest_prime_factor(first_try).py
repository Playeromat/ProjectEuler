import math


def get_primes(number):
    primes = []
    found_divider = False

    for i in range(2, math.ceil(number / 2)):
        for j in range(2, i):
            if i % j == 0:
                found_divider = True
                break

        if found_divider:
            found_divider = False
            continue

        primes.append(i)

    return primes


def print_prime_factors():
    number = 13195
    prime_factors = []
    primes = get_primes(number)

    while number > 1:
        for i, val in reversed(list(enumerate(primes))):
            if val > number / 2:
                primes.pop(i)

            if number % val == 0:
                prime_factors.append(val)
                number = number / val

    print(prime_factors)


print_prime_factors()
