# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 3.4
# Date: 18 09 2025


# variables
a = float(input("Please enter the coefficient A:\n"))
b = float(input("Please enter the coefficient B:\n"))
c = float(input("Please enter the coefficient C:\n"))


# calculate the roots

from math import*


# roots final answer
r1 = (b ** 2 - 4 * a * c)
if a ==0 and b == 0:
       print("You entered an invalid combination of coefficients!")
       1
elif a == 0 and b != 0:
       x = -c / b
       print("The root is x =", x)

elif a > 0:
 r1 = (b ** 2 - 4 * a * c)

 
 if r1 < 0:
     r1 = (b ** 2 - 4 * a * c)
     real= -b/ (2*a)
     imag= sqrt(-r1)/(2*a)
     print("The roots are x =", real, "+", imag, "i and x =", real, "-", imag, "i")
 else:
  s1= r1 **.5
  x1 = (-b + s1) / (2 * a)
  x2 = (-b - s1) / (2 * a)
  if x1 > x2:
      print("The roots are x =", x1, "and x=", x2)
  elif x1 < x1:
      print("The roots are x =", x1, "and x=", x2)
  elif x1 == x2:
      print("The root is x =", x1)



     