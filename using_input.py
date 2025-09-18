# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 3.1
# Date: 9/11/2025
# Reynolds numner
print (" This program calculates the Reynolds number given velocity, length, and viscosity")


velocity = float(input("Please enter the viscosity (m^2/s):"))
length = float(input("Please enter the length (m):"))
viscosity = float(input("Please enter the viscosity (m^2/s): "))

import math 
re = ((velocity * length)/ viscosity)
print ("Reynolds number is", re)

#Bragg's law
print ("This program calculates the wavelength given distance and angle")

distance= float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees):"))
n = 1
import math
wl = ( (2 * distance * math.sin(angle))/ n )
print ("Wavelength is", wl, "nm")
# production rate
print (" This program calculates production rate of a well given a time in days")
t = float(input("Please enter the time (days):"))
ip= float(input("Please enter the initial rate (barrels/day):"))
hc = float(input("Please enter the decline rate (1/day):"))
idr = 1

production_rate =  ip / (1 + hc * idr * t)**(1/hc)
formatted = format(production_rate, ".2f")
print ("Production rate is", formatted, "barrels/day")
# rocket velocity
print (" This program calculates the production rate given time, initial rate, and decline rate")
im = float(input("Please enter the initial mass (kg):"))
fm = float(input("Please enter the final mass (kg):"))
ev = float(input("Please enter the exhaust velocity (m/s):"))
cv = ( ev * math.log(im/fm))
formatted = format(cv,".1f")
print ("Change of velocity is", formatted, "(m/s)")
