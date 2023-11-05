#Non-Recursive
def fibonacci_non_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0] * (n + 1)
        fib[0] = 0
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]

# Test the non-recursive Fibonacci function
n = 12
print(f"Fibonacci({n}) = {fibonacci_non_recursive(n)}")

#Recursive
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test the recursive Fibonacci function
n = 10
print(f"Fibonacci({n}) = {fibonacci_recursive(n)}")
