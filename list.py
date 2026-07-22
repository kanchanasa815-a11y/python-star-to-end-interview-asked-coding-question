#Find largest element
number=[90,80,35,46,70]
number.sort()
print(number[-1])

#Find smallest Element
number=[90,80,35,46,70]
number.sort()
print(number[0])

#other code both small and larger
number=[90,80,35,46,70]
larger_num=max(number)
smaller_num=min(number)
print(larger_num)
print(smaller_num)

#reverse the list
number=[89,54,34,68,90]
number.reverse()
print(number)

#Reverse the String
text=input("Enter the string: ")
reverse_text=text[::-1]  #[start:stop:step]
print(reverse_text)

#Check Palandrom
text=input("Enter the text: ")
if text==text[::-1]:
  

#Remove Duplicate
number=[9,2,3,3,9,7,2]
remove_duplicate=list(set(number))
print(remove_duplicate)

#count frequency of Element
number=[10,20,30,10,20,30,40]
frequency={}
for num in number:
  if num in frequency:
    frequency[num]+=1
  else:
    frequency[num]=1
print(frequency)

#Find the Second Largest Element
number=[90,87,78,56,76,72]
print(number)
number.sort()
print(number)



