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
