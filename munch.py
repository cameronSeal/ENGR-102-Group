num = float(input("enter a 4 digit number:"))
from math import *
d1= num//1000
d2= (num//100)%10
d3= (num-(d1*1000 + d2*100))//10
d4= ((num-(d1*1000 + d2*100 )//10)%10)
print (d1,d2,d3,d4)
munch = (d1**d1) + (d2**d2) + (d3**d3) + (d4**d4)
if munch==num:
    print("munch")
else:
    print("not munch")