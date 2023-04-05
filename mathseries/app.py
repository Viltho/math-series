from series import fibonacci, lucas, sum_series

series = input("Enter the series type (fib/luc/sum): ")

if series == "fib":
    x = input("What is your fibonacci parameter? ")
    input_fib = int(x)
    print(fibonacci(input_fib))
elif series == "luc":
    x = input("What is your lucas parameter? ")
    input_luc = int(x)
    print(lucas(input_luc))
elif series == "sum":
    x = input("What is your sum series parameter? ")
    input_sum = int(x)
    y = input("What is your first optional parameter? ")
    first_optional = int(y)
    z = input("What is your second optional parameter? ")
    second_optional = int(z)
    print(sum_series(input_sum, first_optional, second_optional))
else:
    print("Invalid series type. Please enter fib, luc, or sum.")
