#question1
import time
print(time.gmtime(0))

#question2
import datetime
print(datetime.date.today())
print(time.ctime())

#question3
from datetime import datetime
d=datetime.now()
print(d)
print(d.strftime("%B"))

#question4
from datetime import datetime
now=datetime.now()
print("day:",now.strftime("%A"))

#question5
import datetime
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime()))
l=list(time.localtime())
print(l)
print(l[2])

#question6
import time
print(time.localtime())

#question7
import math 
print(math.factorial(10))

#question8
import math
print(math.gcd(30,50))

#question9
import os
print(os.getcwd())
print(os.name)
print(os.listdir)
print(os.environ)