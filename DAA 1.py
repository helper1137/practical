# Function to count Fibonacci numbers in the given range [low, high]
def countFibs(low, high):
    # Initialize first three Fibonacci Numbers
    f1, f2, f3 = 0, 1, 1

    # Count Fibonacci numbers in the given range
    result = 0

    while f1 < low:
        f1, f2, f3 = f2, f3, f1 + f2

    while f1 <= high:
        result += 1
        f1, f2, f3 = f2, f3, f1 + f2

    return result

# Driver program
low = 10
high = 100
print("Count of Fibonacci Numbers is", countFibs(low, high))


