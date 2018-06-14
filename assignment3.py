#create a list with user defined inputs.
print ("enter the list item")
list=[]
x=input("2")
y=input("3")
z=input("4")
print("the list is")
list=[x,y,z]
print(list)
print("\n")

#Add the following list the above create list{'googal','apple',facebook','microsoft','tesla']
list2=['googal','apple','facebook','microsoft','tesla']
print(list2)
print(list.extend(list2))
print(list)
print("\n")

#count  the number of time on object
list=[1,2,3,2,4,2,5,6,7,2]
list.count(2)
print("\n")

#create a list with number and sort it in ascending order.
l=[1,3,4,6,3,5]
print(l.sort())
print(l)
print("\n")

#question(5)
list3=[1,2,5,3,6,4]
print(list3)
list4=[7,9,11,8,10,12]
print(list4)
list3.sort()
list4.sort()
print(list3)
print(list4)
print("\n")
p1=[list3,list4]
print(p1)
print("\n")

#implement a stack & queues using list
print("stack")
list5=["I","love","Mom"]
print(list5)
print(list5.append("Bhi"))
print(list5)
print(list5.pop())
print(list5)
print("queues")
list6=["I","love","Mom"]
print(list6)
print(list6.append("Bhi"))
print(list6)
del list6[0]
print(list6)

#count even & odd number in that list.
list7=[1,2,3,4,5,6]
even_count=0
odd_count=0
for x in list7:
	if(x%2 == 0):
		even_count=even_count+1
	else:
		odd_count=odd_count+1
	print("count the even number",even_count)
	print("count the odd number ",odd_count)


 


