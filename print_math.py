# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 1.12
# Date: 03 09 2025
#
# calculate and print the reynolds number of a fluid has 
# velocity (U) 9 m/s 
# kenimatic viscocity (V) 0.0015 m^2/s
# characteristic linear dimention (L) 0.875 M
print ("Reynolds number is", (9 * .875) / .0015)
import math 
print ("Wavelength is", 2 * .029 * math.sin(35*math.pi/180), "nm")
from math import*

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