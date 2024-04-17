# Author : Kalpana Sahu
# Version : 1.0
# WAP to input three number and find the largest of three numbers using if statement

n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
n3 = int(input("Enter 3rd number : "))

if n1 > n2 and n1 > n3:
    print("{} is the Largest.".format(n1))

elif n2 > n1 and n2 > n3:
    print("{} is the Largest.".format(n2))
else:
    print("{} is the Largest.".format(n3))
