# Author : Kalpana Sahu
# Version : 1.0
# WAP to input rate of interest, Principle amount and number of years. Then find the simple interest

roi = int(input("Enter rate of interest : "))
amount = int(input("Enter principle amount : "))
time = int(input("Enter time : "))

si = (amount * roi * time) / 100

print("Simple interest is : ", si)
