# Author : Kalpana Sahu
# Version : 1.0
# WAP to read an amount and determine how many notes are required from 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2 and 1 rupee note

amount = int(input("Enter the amount : "))
print("No of 2000 note is {}".format(amount//2000))

amount = amount % 2000
print("No of 1000 note is {}".format(amount//1000))

amount = amount % 1000
print("No of 500 note is {}".format(amount//500))

amount = amount % 500
print("No of 200 note is {}".format(amount//200))

amount = amount % 200
print("No of 100 note is {}".format(amount//100))

amount = amount % 100
print("No of 50 note is {}".format(amount//50))

amount = amount % 50
print("No of 20 note is {}".format(amount//20))

amount = amount % 20
print("No of 10 note is {}".format(amount//10))

amount = amount % 10
print("No of 5 note is {}".format(amount//5))

amount = amount % 5
print("No of 2 note is {}".format(amount//2))

amount = amount % 2
print("No of 1 note is {}".format(amount//1))
