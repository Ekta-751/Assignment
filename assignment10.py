#Perform Inheritance
class animal:
     def animal_attribute(self):
         print("Animal")
class tiger(animal):
     pass
a=tiger()
a.animal_attribute()

#Write The Output of a Code
class A:
    def f(self): 
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())

#Create a Class Cope and Initialize it
class Cop:
	def __init__(self,copname,copage,work_experience,designation):
		self.copname=copname
		self.copage=copage
		self.work_experience=work_experience
		self.designation=designation
	def display(self):
		print("Details:")
		print(self.copname)
		print(self.copage)
		print(self.work_experience)
		print(self.designation)
		
	def update(self,copname,copage,work_experience,designation):
		self.copname=copname
		self.copage=copage
		self.work_experience=work_experience
		self.designation=designation
class Mission(Cop):
	fighter_planes=4
	tankers=7
	def add_mission_details(self):
		print("number of fighter planes:",self.fighter_planes)
		print("number of tankers:",self.tankers)
copname=input("Name:")
copage=int(input("Age:"))
work_experience=input("Work Experience:")
designation=input("Designation:")

a=Mission(copname,copage,work_experience,designation)
print("")
a.display()
print("")
a.add_mission_details()
print("")
a.update(input("Name:"),int(input("Age:")),input("Work Experience:"),input("Designation:"))
print("")
a.display()

 
#Create The Class Shape And Initialize It Initialize it 

class Shape:
	def __init__(self,len,bre):
		self.len=len
		self.bre=bre
		
		
	def area(self):
		self.result=self.len*self.bre
		
		
class Rectangle(Shape):
	def arearectangle(self):
		print("area of rectangle:",self.result)
		
class Square(Shape):
	def areasquare(self):
		print("area of square:",self.result)
		
		
len=int(input("enter the len:"))
bre=int(input("enter the bre:"))
c=Rectangle(len,bre)
b=Square(len,bre)
if len==bre:
	b.area()
	b.areasquare()
else:
	c.area()
	c.arearectangle()
