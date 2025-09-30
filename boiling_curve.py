# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 5.5
# Date: 30 09 2025
#

# This program calculates the boiling point of water 
# by taking the exces temperature

# our otiginal (a,b,c,d,e) values are
ax,ay = (1.3,1e3)
bx,by = (5,7e3)
cx,cy = (30,1.5e6)
dx,dy = (120, 2.5e4)
ex,ey = (1200, 1.5e6)

# math import for log to work
from math import log

# get the excess temperature input 
temp= float(input("Enter the excess temperature: "))

# check if the input is in the valid range
if temp < 1.3 or temp > 1200:
    print("Surface heat flux is not available")
# if the input is valid, we continue
else:
    # calculate the boiling point by each segment

    # a to b
    if temp >= 1.3 and temp < 5:
        m = ((log(by/ay)))/(log(bx/ax))
        boiling_point = ay * ((temp/ax)**m)
        rounded_q = round(boiling_point)
        print("The surface heat flux is approximately", rounded_q, "W/m^2")
    # b to c
    elif temp >= 5 and temp < 30:
        m = ((log(cy/by)))/(log(cx/bx))
        boiling_point = by * ((temp/bx)**m)
        rounded_q = round(boiling_point)
        print("The surface heat flux is approximately", rounded_q, "W/m^2")
    # c to d
    elif temp >= 30 and temp < 120:
        m = ((log(dy/cy)))/(log(dx/cx))
        boiling_point = cy * ((temp/cx)**m)
        rounded_q = round(boiling_point)
        print("The surface heat flux is approximately", rounded_q, "W/m^2")
    # d to e
    elif temp >= 120 and temp <= 1200:
        m = ((log(ey/dy)))/(log(ex/dx))
        boiling_point = dy * ((temp/dx)**m)
        rounded_q = round(boiling_point)
        print("The surface heat flux is approximately", rounded_q, "W/m^2")
