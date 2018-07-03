#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import tkinter
from tkinter import *
print("hello world")
def display():
	exit(0)
root=Tk()
b=Button(root,text="exit",width=35,bg='red',fg='white',command=display)
b.pack()
root.mainloop()

#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
import tkinter
from tkinter import *
def display():
	print("hello world")
	exit(0)
root=Tk()
b=Button(root,text="exit",width=35,bg='red',fg='white',command=display)
b.pack()
root.mainloop()

#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
import tkinter
from tkinter import *
def disply():
	label.config(text = "Hello Python")
root=Tk()
label=Label(root,text="Hello World",width=30,) 
label.pack()
f1=Frame(root)
f1.pack()
b1=Button(f1,width=25,text="button")
b1.pack()
b2=Button(f1,width=25,text="change", command= disply)
b2.pack()
root.mainloop()

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
import tkinter
from tkinter import *
def show():
	a=entry1.get()
	b=entry2.get()
	label=Label(root,text=a)
	label.grid(row=2,column=1)
	label1=Label(root,text=b)	
	label1.grid(row=2,column=2)
root=Tk()
label1=Label(root,text='RealName',width=25)
label1.grid(row=0)
label2=Label(root,text='NikName',width=25)
label2.grid(row=1)
b1=Button(root,width=25,text="hello world",command=show)
b1.grid()
entry1=Entry(root,width=25)
entry1.grid(row=0,column=1)
entry2=Entry(root,width=25)
entry2.grid(row=1,column=1)
root.mainloop()
