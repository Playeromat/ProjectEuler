def print_prime_factors():
    number = 600851475143
    temp = number
    prime_factors = []
    last_prime_number = 1

    while True:
        prime_number = get_next_prime_number(last_prime_number, number)

        if temp < prime_number:
            break

        if temp % prime_number == 0:
            prime_factors.append(prime_number)
            temp /= prime_number

        last_prime_number = prime_number

    print(prime_factors)


def get_next_prime_number(last_prime_number, max):
    found_divider = False

    for i in range(last_prime_number + 1, max):
        for j in range(2, i):
            if i % j == 0:
                found_divider = True
                break

        if found_divider:
            found_divider = False
            continue

        return i
