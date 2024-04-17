# Author : Kalpana Sahu
# Version : 1.0
# WAP to read a number and check that the number is either positive or negative or zero

n = int(input("Enter a number : "))

if n > 0:
    print("{} is positive.".format(n))
elif n < 0:
    print("{} is negative.".format(n))
else:
    print("{} is zero.".format(n))
