# Factorial of a number

# Method - 1 = NORMAL
n = int(input("Enter a number : "))
result = 1
if n == 0 or n == 1:
    print(result)
for i in range(2,n+1):
    result *= i
print(result)

# Method - 2 = RECURSION
x = int(input("Enter a number : "))
def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(x))