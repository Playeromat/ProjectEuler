import math


def print_largest_palindrome_product():
    max_factor = 99999
    palindrome = get_next_palindrome(max_factor * max_factor)

    while True:
        product = get_product(palindrome, max_factor)

        if not product:
            palindrome = get_next_palindrome(palindrome)
        else:
            break

    print(str(product) + " * " + str(int(palindrome / product)) + " = " + str(int(palindrome)))


def get_product(palindrome, max_factor):
    first_factor = max_factor
    second_factor = 0

    while second_factor < max_factor:
        if palindrome % first_factor == 0:
            return first_factor

        first_factor -= 1
        second_factor = palindrome / first_factor

    return False


def get_next_palindrome(number):
    new_palindrome = int(number) - 1
    number_array = list(str(new_palindrome))
    digits = len(number_array)
    offset_changed = False

    i = 0
    while i < digits:
        number_array = list(str(int(new_palindrome)))
        offset = int(number_array[i]) - int(number_array[digits - (i + 1)])

        if offset > 0:
            offset_changed = True
            offset -= 10

        new_palindrome += offset * math.pow(10, i)

        i += 1

        if offset_changed:
            i = 0
            offset_changed = False

    return new_palindrome


print_largest_palindrome_product()