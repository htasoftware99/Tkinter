from cgitb import enable
from tkinter import *
root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()


def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()
    

myButton = Button(root, text="Enter your name", padx=50, pady=50, command=myClick)
myButton.pack()
root.mainloop()