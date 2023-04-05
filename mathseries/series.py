def fibonacci(n):
    a, b = 0, 1
    fib = [a, b]
    for i in range(n):
        a, b = b, a + b
        fib.append(b)
        if len(fib) == n+2:
            print(f"The fib series is: {fib}")
            print(f" and for your parameter {n} the value is ")

    return b

def lucas(n):
    a, b = 2, 1
    luc = [a, b]
    for i in range(n):
        a, b = b, a + b
        luc.append(b)
        if len(luc) == n+2:
            print(f"The lucas series is: {luc}")
            print(f" and for your parameter {n} the value is ")
    return b

def sum_series(n, a, b):
    sum = [a, b]
    for i in range(n):
        a, b = b, a + b
        sum.append(b)
        if len(sum) == n+2:
            print(f"The sum series is: {sum}")
            print(f" and for your parameter {n} the value is ")
    return b

