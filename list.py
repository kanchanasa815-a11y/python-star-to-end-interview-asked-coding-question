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

#Check Pailandrom
text=input("Enter the text: ")
if text==text[::-1]:
  print("Pailandrom")
else:
  print("Not pailandrom")
  
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

#Marge of Two List
Marge of the Two list using oparator(+),extand(),append(),unpacking(*)
#Marge using operator(+)                    #marge using extand()
list1=[1,2,3,4,5]                        list1=[1,2,3,4,5]
list2=[6,7,8,9,0]                        list2=[6,7,8,9,0]          
marge_list=list1+list2       or          list1.extend(list2)
print(marge_list)                        print(list1)

#Marge using append()
list1=[1,2,3,4,5]                        
list2=[6,7,8,9,0]
for item in list2:
  list1.append(item)
  print(list1)
  
#Marge using Unpacking(*)
list1=[1,2,3,4,5]                        
list2=[6,7,8,9,0]
marge_list=[*list1,*list2]
print(marge_list)

#Rotate list by K position
number=[10,20,30,40,50]
k=int(input("Enter a K: "))
k=k%len(number)
rotate=number[-k:]+number[:-k]
print("Rotate= ",rotate)

#Moves Zero to End
number=[2,0,3,0,0,0,5,6]
result=[]
for num in number:
  if num!=0:
    result.append(num)
zeros=len(number)-len(result)
result.extend([0]*zeros)
print(result)

#Find the one Missing number
number=[1,2,3,4,6]
n=len(number)+1
expected_sum=n*(n+1)//2
actual_sum=sum(number)
missing=expected_sum-actual_sum
print("Missing Number:",missing)

#Findimg all missing number
number=[1,2,5,7,9]
missing=[]
for i in range(1,max(number)+1):
  if i not in number:
    missing.append(i)
print("missing Number:",missing)

#finding common Element
list1=[10,20,30,40,50]
list2=[60,10,20,70,30]
common=[]
for i in list1:
  if i in list2:
    common.append(i)
    print(common)
     (or)
list1=[10,20,30,40,50]
list2=[60,10,20,70,30]
for i in list1:
  if i in list2:
    print(i)
    
#check the sorted number
numbers=[10,20,90,70,40,30]
if numbers==sorted(numbers):
  print("Number is sorted")
else:
  print("Number is not sorted")

#Remove even number
number=[1,2,3,4,5,6,7,8,9]
odd=[i for i in number if i%2!=0]
print(odd)

#Find the maximun number
number=[20,30,40,50,80,100]
number.sort
print(number[-1])
        (or)
number=[20,30,40,50,80,100]
num=max(number)
print(num)

#Sum of all Numbers
numbers=[2,3,4,5,6,7,8]
total=sum(numbers)
print("sum= " ,total)


