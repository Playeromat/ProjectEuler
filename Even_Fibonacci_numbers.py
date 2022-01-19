def print_even_fibonacci_sum():
    fibonacci = [1, 2]
    sum = 0

    while True:
        next_fibo = fibonacci[len(fibonacci) - 2] + fibonacci[len(fibonacci) - 1]

        if next_fibo > 4000000:
            break

        fibonacci.append(next_fibo)

    for idx, val in enumerate(fibonacci):
        if fibonacci[idx] % 2 == 0:
            sum += fibonacci[idx]

    print(sum)
