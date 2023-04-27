# Cade Kirkpatrick
# 02-09-2023
#The approximation is 1.618033988205325 after using 9 as m for accuracy.

# Function to calculate the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Function to calculate the ratio between two Fibonacci numbers
def golden_ratio(fib_n, fib_n_1):
    return fib_n/fib_n_1

# Function to calculate the ratio of consecutive Fibonacci numbers until the desired precision is reached
def calculate_fibonacci_ratio(precision):
    # Define the first two Fibonacci numbers
    fib_n_1 = 1
    fib_n = 1
    # Calculate the initial ratio of the first two Fibonacci numbers
    ratio = golden_ratio(fib_n, fib_n_1)
    # Initialize the index to 2, as the first two Fibonacci numbers have already been calculated
    index = 2
    # Initialize the exact value of the Golden Ratio
    phi = (1 + 5**0.5)/2

    # Continue calculating the next Fibonacci numbers and their ratio until the desired precision is reached
    while abs(ratio - phi) > precision:
        # Calculate the next Fibonacci number
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
        fib_n = fib_n_1 + fib_n_2
        # Calculate the ratio of the consecutive Fibonacci numbers
        ratio = golden_ratio(fib_n, fib_n_1)
        # Increment the index
        index += 1

    # Return the index and the ratio of the consecutive Fibonacci numbers
    return index, ratio

# Read the value of M from the user
m = int(input("Enter the value of M: "))
# Calculate the desired precision using 10^-M
precision = 10**-m
# Calculate the number of Fibonacci terms required to attain the desired precision
index, ratio = calculate_fibonacci_ratio(precision)

print("The approximation of the golden ratio is", ratio, "after approximating using", m, "as m for accuracy.")