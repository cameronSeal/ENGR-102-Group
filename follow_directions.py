# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 1.13
# Date: 03 09 2025
#


print ("This shows the evaluation of ( 1 - cos(x)) /x^2 evaluated close to x=0 ")
print ("My guess is 0")
#moveing the decibal 1 place over each place, as to get closer to 0
import math 
x1=1
x2=.1
x3=.01
x4=.001
x5=.0001
x6=.00001
x7=.000001
x8=.0000001

print ("\n")
results= ( 1 - math.cos( x1 )) / (x1 ** 2)
print (results)

results= ( 1 - math.cos( x2 )) / (x2 ** 2)
print (results)

results= ( 1 - math.cos( x3 )) / (x3 ** 2)
print (results)

results= ( 1 - math.cos( x4 )) / (x4 ** 2)
print (results)

results= ( 1 - math.cos( x5 )) / (x5 ** 2)
print (results)

results= ( 1 - math.cos( x6 )) / (x6 ** 2)
print (results)

results= ( 1 - math.cos( x7 )) / (x7 ** 2)
print (results)

results= ( 1 - math.cos( x8 )) / (x8 ** 2)
print (results)
print ("\n")

print(" My guess was slightly off of the appropriate result")
