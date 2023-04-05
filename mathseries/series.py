def lucas(n):
    a, b = 2, 1
    luc = [a, b]
    for i in range(n):
        a, b = b, a + b
        luc.append(b)
        if len(luc) == n+2:
            print(f"The lucas series is: {luc}")
    return f"for your parameter {n} the value is {b}"

def sum_series(n, a, b):
    sum = [a, b]
    for i in range(n):
        a, b = b, a + b
        sum.append(b)
        if len(sum) == n+2:
            print(f"The sum series is: {sum}")
    return f"for your parameter {n} the value is {b}"

