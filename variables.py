#swaping two numbers

a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
print(a,b)
temp=a
a=b
b=temp
print(a,b)

#other method [swaping two numbers without using the third variable]
a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
print(a,b)
a,b=b,a
print(a,b)

#other method
a=8
b=9
print(a,b)
a,b=b,a
print(a,b)

#find the data type of a variable
a="string"
b=0.99
c=90
d=True
e=[1,2,3,4]
f=(4,5,6,7)
g={"apple","banana","graps"}
h={"name":"kanchana","age":22,"stading":"B.E"}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(e))
print(type(h))

# Input name and age and display them
name=input("Enter the name: ")
age=int(input("Enter the age: "))
print(name)
print(age)

#Calculate simple interest
p=float(input("Enter the principal amount: "))
r=float(input("ENter the rate of interest: "))
t=float(input("Enter the time: "))

simple_interest=(p*r*t)/100

print("simple interest= ",simple_interest)

#Calculate the area of circle
r=int(input("Enter the radius:"))
area_of_circle=3.14*r*r
print("Area of circle=",area_of_circle)

#other method of the area of the circle
import math
radius=float(input("Enter the radius: ")
area_of_circle=math.pi*radius*radius
print("Area of circle:",area_of_circle)
             




