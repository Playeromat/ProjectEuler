if __name__ == '__main__':
    from timeit import Timer

    def get_time(function_name, file_name):
        t = Timer(function_name + "()", "from " + file_name + " import " + function_name)
        return t.timeit(1)


    # print(get_time("print_multiplies_sum", "Multiples_of_3_or_5"))
    # print(get_time("print_even_fibonacci_sum", "Even_Fibonacci_numbers"))
    # print(get_time("print_prime_factors", "Largest_prime_factor"))
