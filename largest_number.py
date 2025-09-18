# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 4.1
# Date: 18 09 2025
#
# this code is going to choose the largest number
num1= float(input("Enter number 1:\n"))
num2= float(input("Enter number 2:\n"))
num3= float(input("Enter number 3:\n"))
# compare the numbers
if num1>=num2 and num1>=num3:
    print("The largest number is",num1)
elif num2>=num1 and num2>=num3:
    print("The largest number is",num2)
else:
    print("The largest number is",num3)