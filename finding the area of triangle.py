
import math
print("area of triangle with sides   ")
a=input("enter length of first side   ")
b=input("enter the length of second side  ")
c=input("enter the lenght of third side  ")
p=(a+b+c)/2  #half of the perimeter
x=p-a
y=p-b
z=p-c
t=p*x*y*z
area=math.sqrt(t)
print("area of triangle is" , area)


	
