# Largest among 3 variables

# INPUT
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if (num1 == num2 and ((num1 and num2) > num3)):
    print("First and Second are equal and Third is the Smallest")
elif (num1 == num2 and ((num1 and num2) < num3)):
    print("First and Second are equal and Third is the Largest")
elif (num1 == num3 and ((num1 and num3) > num2)):
    print("First and Third are equal and Second is the Smallest")
elif (num1 == num3 and ((num1 and num3) < num2)):
    print("First and Third are equal and Second is the Largest")
elif (num2 == num3 and ((num3 and num2) > num1)):
    print("Second and Third are equal and First is the Smallest")
elif (num2 == num3 and ((num3 and num2) < num1)):
    print("Second and Third are equal and First is the Largest")
elif (num1 > num2 and num1 > num3):
    print(f"{num1} i.e. First is the Largest")
elif (num2 > num1 and num2 > num3):
    print(f"{num2} i.e. Second is the Largest")
elif (num3 > num1 and num3 > num2):
    print(f"{num3} i.e. Third is the Largest")
else:
    print("All are equal")