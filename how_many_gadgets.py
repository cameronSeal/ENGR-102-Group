# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 3.4
# Date: 03 09 2025

day = int(input("Please enter a positive value for day:\n"))
# decide where the day falls in the ranges and calculate accordingly
if day <= 0 :
    print("You entered an invalid number!")
elif 0 <= day <= 10 :
    print("The sum total number of gadgets produced on day", day, "is", (day * 10))
elif 10 < day <= 50 :
    print("The sum total number of gadgets produced on day", day, "is", (100 + (((day - 10) * (day + 11)) // 2)))
elif 50 < day <= 101 :
    print("The sum total number of gadgets produced on day", day, "is", (100+ 1170 + (50 * (day - 49))))
else :
    print("The sum total number of gadgets produced on day", day, "is", "3820")
