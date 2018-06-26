#1. Name and handle the exception occured in the following program: 
#ZeroDivisionError
try:
    a=3
    if a<4:
     a=a/(a-3)
     print(a)
except Exception:
     print("Exception occured")

#2. Name and handle the exception occurred in the following program: 
l=[1,2,3]
try:
    print([3])
except Exception:
      print("Exception occured")
print("IndexError")

#3.What will be the output of the following code:
#Program to depict Raising Exception
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not
#output:
# An exception
# Traceback (most recent call last):
  # File "assignment13.py", line 22, in <module>
    # raise NameError("Hi there")  # Raise Error
# NameError: Hi there

#4.What will be the output of the following code:

 #Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
# output:-5.0
#        a/b result in 0

#5.Write a program to show and handle following exceptions: 
# 1. Import Error
# 2. Value Error
# 3. Index Error
#1.Import Error
try:
    from exception import MyException
except Exception as e:
    print(e)
#2.value Error
try:
    raise ValueError("An Exception is raised")
except Exception as e:
    print(e)
#Index Error
l=[1,2,3]
try:
     print(l[5])
except ZeroDivisionError:
     print("dovision by zero")
except IndexError:
     print("Index Error")

#6.Create a user-defined exception:
class ValueTooSmallError(Exception):
      pass
while True:
   try:
      i_num=int(input("enter a number"))
      if i_num < 18:
        raise ValueTooSmallError("exception")
      else:
        print("eligible")
        break
   except ValueTooSmallError as e:
        print("this value is too samll ,try again!")
        print(e)
