# Number of test cases
T =  int(input(""))

# Function to find the sum of even Fibonacci numbers up to a large N
def sum_even_fibonacci_large(N):
    a, b = 0, 2  # First two even Fibonacci numbers
    sum_of_even_fib = a + b

    # Generate even Fibonacci numbers directly and sum them until N is reached
    while True:
        next_even_fib = 4 * b + a
        if next_even_fib > N:
            break
        sum_of_even_fib += next_even_fib
        a, b = b, next_even_fib

    return sum_of_even_fib

# Process each test case
for _ in range(T):
    N =  int(input(""))
    result = sum_even_fibonacci_large(N)
    print(result)
