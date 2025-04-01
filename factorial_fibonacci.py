# Factorial Calculation
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Fibonacci Calculation
def fibonacci(n):
    if n <= 0:
        return "Fibonacci not defined for negative numbers or zero"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = [0, 1]
        while len(series) < n:
            series.append(series[-1] + series[-2])
        return series



        # Main Program
num = int(input("Enter a number: "))

print(f"Factorial of {num} is {factorial(num)}")
print(f"First {num} numbers of the Fibonacci series: {fibonacci(num)}")