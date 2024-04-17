# Author : Kalpana Sahu
# Version : 1.0
# WAP to read a number and check whether it is even number or odd number

n = int(input("Enter a number : "))

if n % 2 == 0:
    print("{} is an even number.".format(n))
else:
    print("{} is a odd number.".format(n))
