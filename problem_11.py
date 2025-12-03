# Check Prime Number

# INPUT
num = int(input("Enter a Number : "))

if num == 0 or num == 1:
    print("Not a prime number")

if num > 1:
    for i in range(2,num):
        if ( num % i == 0):
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Enter a positive valid number")
