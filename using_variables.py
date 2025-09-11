# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 2.9
# Date: 03 09 2025
#
#
# calculate/print the area of a rectangle of length 5 in and 
# height 3 in
length = 5 # inches
height= 3 # inches
area= length * height #inches^2

print ()

U= 9 # m/s 
V= 0.0015 # m^2/s
L= .875 #m
print ("Reynolds number is", (U * L) / V)

d=.029
A=35
import math 
print ("Wavelength is", 2 * d * math.sin(A*math.pi/180), "nm")

qi= 100
t=10
di=2
b=.8
t=10
print ("Production rate is", qi / (1 + (b * di * t)) ** (1 / b), "barrels/day")

mo= 11000
mf= 8300
ve= 2029
print ("Change of velocity is", ve * math.log( mo/ mf ), "m/s")