#swaping two numbers
a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
print(a,b)
temp=a
a=b
b=temp
print(a,b)

#other method
a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
print(a,b)
a,b=b,a
print(a,b)

#other methon
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
