#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the
dictionary.
import tkinter
from tkinter import *
d={'ekta':9034069410,'deepa':9671246560,'divya':7015303696}
root=Tk()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for key in d.values():
	l.insert(END,'this i9s the list no'+str(key))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()
 
# Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.
import tkinter
from tkinter import *
d={'ekta':9034069410,'deepa':9671246560,'divya':7015303696}
def insert():
	k=entry1.get()
	v=entry2.get()
	d[k]=v
	l.insert(END,k)
	print(d)
root=Tk()
entry1=Entry(root)
entry1.pack()
entry2=Entry(root)
entry2.pack()
b=Button(root,text="insert",command=insert)
b.pack()
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
l=Listbox(root,yscrollcommand=s.set)
for key in d.values():
	l.insert(END,'this i9s the list no'+str(key))
l.pack(side=LEFT,fill=BOTH)
s.config(command=l.yview())
root.mainloop()