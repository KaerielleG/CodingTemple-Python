#task1
# Prompt the user to enter three numbers
num=13
num=18
num=22

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

#task2
num1=12
num2=14
num3=16

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if(num1 <= num2) and (num1 <=num3):
    smallest = num1
elif (num2 <= num1) and (num <= num3):
   smallest = num2
else: 
   smallest = num3

print("The smallest number is", smallest)


#task3
num1=20
num2=30
num3=30

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 == num3:
 print("All numbers are equal.")
elif num1 == num2:
    if num1 < num3:
        print("First and second numbers are equal and the smallest.")
    else:
        print("First and second numbers are equal and larger than the third number.")
elif num1 == num3:
    if num1 < num2:
        print("First and third numbers are equal and the smallest.")
    else:
        print("First and third numbers are equal and larger than the second number.")
elif num2 == num3:
    if num2 < num1:
        print("Second and third numbers are equal and the smallest.")
    else:
        print("Second and third numbers are equal and larger than the first number.")
else:
    # Determine the smallest number when they are not equal
    if (num1 <= num2) and (num1 <= num3):
        smallest = num1
    elif (num2 <= num1) and (num2 <= num3):
        smallest = num2
    else:
        smallest = num3
    print("The smallest number is", smallest)


