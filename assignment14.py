#1.rite a Python program to read last n lines of a file.
f=open("test.txt")ds
content=f.readlines()
print(content)
f.close()
n=int(input("enter the cantant of index we want to read at a last"))
while n>0:
    print(content[-n])
    n=n-1

#2.ite a Python program to count the frequency of words in a file.
words=open("test.txt","r").read().split() #read the words into a list.
print(words)
print(type(words))
uniqWords=sorted(set(words)) #remove duplicate words and sort
print(uniqWords)
print(type(uniqWords))
for word in uniqWords:
	print(word.count(word),word)

#3.rite a Python program to copy the contents of a file to another file.
with open('test.txt','r') as f1:
	with open('test1.txt','w') as f2:
		for line in f1:
			f2.write(line)

#4.ite a Python program to combine each line from first file with the corresponding line in second file.
with open('test.txt','r') as f1:
	with open('test1.txt','r') as f2:
		for line1,line2 in zip(f1,f2):
			print(line1+line2)

# 5.ite a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
f=open('test2.txt','r+')
for i in range(10):
	x=str(random.randint(1,100))
	f.write(x+"\n")
l=f.readlines()
print(l)
l.sort()
print(l)
with open('test3.txt','r+')as f2:
	for n in l:
		f2.write(n)
f.close()
