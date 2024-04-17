# Author : Kalpana Sahu
# Version : 1.0
# WAP to input number of second and disply number of hour and minute

second = int(input("Enter the second : "))
print("Hour is {}".format(second // 3600))

second = second % 3600
print("Minute is {}".format(second // 60))

second = second % 60
print("Minute is {}".format(second))
