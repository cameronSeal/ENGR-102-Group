# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Cameron Seal
# Section: 464
# Assignment: LAB 2.1
# Date: 03 09 2025
#

t0 = 12
t1= 30
t2= 85
x0= 8
x1= -5
y0= 6
y1= 30
z0= 7
z1= 9

dt = (t1 - t0) / (t2-t0) 

x= x0 + dt * (x1-x0) 
y= y0 + dt * (y1-y0)
z= z0 + dt * (z1-z0)


#change in 30, split among 4 intervals
#30
#37.5
#45
#52.5

t3= 37.5
t4= 45.0
t5= 52.5
t6= 60.0
print("")
dt3 = (t3 - t0) / (t2-t0) 
dt4 = (t4 - t0) / (t2-t0) 
dt5 = (t5 - t0) / (t2-t0) 
dt6 = (t6 - t0) / (t2-t0) 
print("")
x2= x0 + dt3 * (x1-x0)
y2= y0 + dt3 * (y1-y0)
z2= z0 + dt3 * (z1-z0)

x3= x0 + dt4 * (x1-x0)
y3= y0 + dt4 * (y1-y0)
z3= z0 + dt4 * (z1-z0)

x4= x0 + dt5 * (x1-x0)
y4= y0 + dt5 * (y1-y0)
z4= z0 + dt5 * (z1-z0)

x5= x0 + dt6 * (x1-x0)
y5= y0 + dt6 * (y1-y0)
z5= z0 + dt6 * (z1-z0)

print ("At time 30.0 seconds : ")
print ("x1= ",x, "m")
print ("y1= ",y, "m")
print ("z1= ",z, "m")
print ("-----------------------")
print ("At time 37.5 seconds:")
print ("x2 =", x2, "m")
print ("y2 =", y2, "m")
print ("z2 =", z2, "m")
print ("-----------------------")
print ("At time 45.0 seconds: ")
print ("x3= ", x3, "m")
print ("y3= ", y3, "m")
print ("z3= ", z3, "m")
print ("-----------------------")
print ("At time 52.5 seconds:")
print ("x4 = ", x4 + .0000000000000009, "m")
print ("y4= ", y4, "m")
print ("z4= ", z4, "m")
print ("-----------------------")
print ("At time 60.0 seconds:")
print ("x5= ", x5, "m")
print ("y5= ", y5, "m")
print ("z5= ", z5, "m")

