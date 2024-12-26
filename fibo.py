def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    
    return fib_sequence


if __name__ == "__main__":
    terms = 10
    fib_series = fibonacci(terms)
    print(f"The first {terms} terms of the Fibonacci series are: {fib_series}")
