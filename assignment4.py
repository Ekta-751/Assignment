#Question 1
t=(1,2,3,4,5)
print(t)
print(len(t))
print("\n")

#Question2
t1=(1,2,3,4,5)
print(t1)
print(max(t1))
print(min(t1))
print("\n")

# Question3
def pro(t):
    r=1
    for i in t:
        r=r*i
    return r*i
tu=(1,2,3)
p=pro(tu)
print(p)

#Question4
x=int(input("enter the values in set1"))
a=input("1")
b=input("2")
c=input("3")
s1=set([a,b,c])
print(s1)
y=int(input("enter the value in set2"))
d=input("4")
e=input("5")
f=input("6")
s2=set([d,e,f])
print(s2)
print(s1-s2)
print("\n")
print(s1&s2)
print("\n")

Question5
d={}
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
name =str(input("enter name of students"))
marks=int(input("enter marks of students"))
d[name]=marks
print(d)

#Question5
print(d)
value_list=list(d.value())
value_list.sort()
print(value_list)

Question6
l=list("MISSISSPPI")
d={}
d['M']=l.count('M')
d['I']=l.count('I')
d['S']=l.count('S')
d['P']=l.count('P')
print(d)