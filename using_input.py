# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 3.1
# Date: 9/11/2025

print ("This program calculates the Reynolds number given velocity,")
print ("length, and viscosity")

velocity = int(input("Please enter the velocity ( m/s ): "))
length = int(input("Please enter the length ( m ): "))
viscosity = int(input("Please enter the viscosity ( m^2/s ): "))

import math 
re = ((velocity * length)/ viscosity)
print ("Reynolds number is", re)

print ("This program calculates the wavelength given distance and angle")

distance= int(input("Please enter the distance ( nm ):"))
angle = int(input("Please enter the angle ( deegrees ):"))
n = 1
import math
wl = ( (2 * distance * math.sin(angle))/ n )
print ("wavelength is", wl, "nm")

print (" This program calculates production rate of a well given a time in days")
ip= int(input("Please enter the initial production rate ( barrels/ day ):"))
t = int(input("Please enter the quantity of days ( days ):"))
idr = 1
hc = .8
production_rate =  ip / (1 + .8 * idr * t)**(1/.8)
formatted = format(production_rate, ".2f")
print (" the production rate after", t, "days is", formatted, "barrels per day")

print (" This program calculates the change of velocity of an object, using initial mass, final mass and exhaust velocity")
im = int(input("Please enter the initial mass ( kgs ):"))
fm = int(input("Please enter the final mass ( kgs ):"))
ev = int(input("Please enter the exhaust vlocity ( m/s ):"))
cv = ( ev * math.log(im/fm))
formatted = format(cv,".1f")
print ("The change in velocity of the rocket is", formatted, "( m/s )")
